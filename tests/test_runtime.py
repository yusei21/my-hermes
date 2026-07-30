import pytest

from my_hermes import InvalidTransitionError, Task, TaskState


def test_valid_execution_path_records_history() -> None:
    task = Task(objective="Implement a verified feature")

    task.transition(TaskState.PLANNING, reason="Planning started")
    task.transition(TaskState.EXECUTING, reason="Plan accepted")
    task.transition(TaskState.REVIEWING, reason="Implementation completed")
    task.transition(TaskState.VERIFYING, reason="Review passed")
    task.transition(TaskState.SUCCEEDED, reason="Acceptance criteria passed")

    assert task.is_terminal
    assert task.state is TaskState.SUCCEEDED
    assert len(task.events) == 5
    assert task.events[0].previous_state is TaskState.CREATED
    assert task.events[-1].new_state is TaskState.SUCCEEDED


def test_invalid_transition_is_rejected_without_mutation() -> None:
    task = Task(objective="Do not skip planning")

    with pytest.raises(InvalidTransitionError):
        task.transition(TaskState.SUCCEEDED, reason="Invalid shortcut")

    assert task.state is TaskState.CREATED
    assert task.events == []


def test_terminal_task_cannot_transition() -> None:
    task = Task(objective="Cancelled task")
    task.transition(TaskState.CANCELLED, reason="Cancelled by user")

    with pytest.raises(InvalidTransitionError):
        task.transition(TaskState.PLANNING, reason="Attempted restart")
