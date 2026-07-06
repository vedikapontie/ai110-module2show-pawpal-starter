from datetime import datetime, timedelta

from pawpal_system import Pet, Scheduler, Task


def test_sorting_correctness():
    # Create a few tasks with intentionally out-of-order times to verify chronological sorting.
    tasks = [
        Task(title="Dinner", time="14:00"),
        Task(title="Morning Walk", time="08:00"),
        Task(title="Vet Visit", time="11:00"),
    ]

    sorted_tasks = Scheduler().sort_by_time(tasks)

    assert [task.time for task in sorted_tasks] == ["08:00", "11:00", "14:00"]


def test_recurrence_logic():
    # Create a daily task and mark it complete to confirm a new daily instance is generated for the next day.
    pet = Pet(pet_id="pet-1", name="Mochi", species="dog", age=3)
    due_date = datetime.now()
    task = Task(title="Morning Walk", time="07:30", frequency="Daily", due_date=due_date)
    pet.add_task(task)

    next_task = task.mark_complete(pet=pet)

    assert task.completion_status is True
    assert next_task is not None
    assert next_task is not task
    assert next_task.completion_status is False
    assert next_task in pet.tasks
    assert next_task.due_date == due_date + timedelta(days=1)


def test_conflict_detection():
    # Pass multiple tasks sharing the same clock time to ensure duplicate scheduling is detected.
    scheduler = Scheduler()
    tasks = [
        Task(title="Feed Breakfast", time="08:00"),
        Task(title="Morning Walk", time="08:00"),
        Task(title="Medicine", time="09:00"),
    ]

    warning = scheduler.check_conflicts(tasks)

    assert warning is not None
    assert "08:00" in warning
    assert "Warning" in warning
