"""Durable task state and transition validation."""

from __future__ import annotations

from datetime import UTC, datetime
from enum import StrEnum
from uuid import UUID, uuid4

from pydantic import BaseModel, ConfigDict, Field


class TaskState(StrEnum):
    CREATED = "created"
    PLANNING = "planning"
    AWAITING_APPROVAL = "awaiting_approval"
    EXECUTING = "executing"
    REVIEWING = "reviewing"
    VERIFYING = "verifying"
    REPLANNING = "replanning"
    SUCCEEDED = "succeeded"
    FAILED = "failed"
    CANCELLED = "cancelled"


TERMINAL_STATES = {TaskState.SUCCEEDED, TaskState.FAILED, TaskState.CANCELLED}

ALLOWED_TRANSITIONS: dict[TaskState, frozenset[TaskState]] = {
    TaskState.CREATED: frozenset({TaskState.PLANNING, TaskState.CANCELLED}),
    TaskState.PLANNING: frozenset(
        {TaskState.AWAITING_APPROVAL, TaskState.EXECUTING, TaskState.FAILED, TaskState.CANCELLED}
    ),
    TaskState.AWAITING_APPROVAL: frozenset(
        {TaskState.EXECUTING, TaskState.FAILED, TaskState.CANCELLED}
    ),
    TaskState.EXECUTING: frozenset(
        {TaskState.REVIEWING, TaskState.VERIFYING, TaskState.REPLANNING, TaskState.FAILED, TaskState.CANCELLED}
    ),
    TaskState.REVIEWING: frozenset(
        {TaskState.VERIFYING, TaskState.REPLANNING, TaskState.FAILED, TaskState.CANCELLED}
    ),
    TaskState.VERIFYING: frozenset(
        {TaskState.SUCCEEDED, TaskState.REPLANNING, TaskState.FAILED, TaskState.CANCELLED}
    ),
    TaskState.REPLANNING: frozenset(
        {TaskState.EXECUTING, TaskState.AWAITING_APPROVAL, TaskState.FAILED, TaskState.CANCELLED}
    ),
    TaskState.SUCCEEDED: frozenset(),
    TaskState.FAILED: frozenset(),
    TaskState.CANCELLED: frozenset(),
}


class InvalidTransitionError(ValueError):
    """Raised when a task attempts an invalid state transition."""


class TaskEvent(BaseModel):
    model_config = ConfigDict(frozen=True)

    occurred_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    previous_state: TaskState
    new_state: TaskState
    reason: str = Field(min_length=1, max_length=2_000)


class Task(BaseModel):
    """Persistent task aggregate with an append-only transition history."""

    model_config = ConfigDict(validate_assignment=True)

    id: UUID = Field(default_factory=uuid4)
    objective: str = Field(min_length=1, max_length=20_000)
    state: TaskState = TaskState.CREATED
    created_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(UTC))
    events: list[TaskEvent] = Field(default_factory=list)

    @property
    def is_terminal(self) -> bool:
        return self.state in TERMINAL_STATES

    def transition(self, new_state: TaskState, *, reason: str) -> TaskEvent:
        allowed = ALLOWED_TRANSITIONS[self.state]
        if new_state not in allowed:
            raise InvalidTransitionError(
                f"Transition from {self.state.value!r} to {new_state.value!r} is not allowed"
            )

        event = TaskEvent(previous_state=self.state, new_state=new_state, reason=reason)
        self.state = new_state
        self.updated_at = event.occurred_at
        self.events.append(event)
        return event
