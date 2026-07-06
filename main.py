from pawpal_system import Owner, Pet, Scheduler, Task


def main() -> None:
    owner = Owner(owner_id="owner-1", name="Jordan", email="jordan@example.com")

    mochi = Pet(pet_id="pet-1", name="Mochi", species="dog", age=3)
    luna = Pet(pet_id="pet-2", name="Luna", species="cat", age=2)

    owner.add_pet(mochi)
    owner.add_pet(luna)

    walk_task = Task(title="Morning Walk", description="Walk around the park", time="07:30", frequency="Daily")
    feed_task = Task(title="Feed Breakfast", description="Serve breakfast and fresh water", time="08:00", frequency="Daily")
    play_task = Task(title="Play Session", description="Interactive playtime", time="18:00", frequency="Daily")
    litter_task = Task(title="Clean Litter Box", description="Clean the litter box", time="20:00", frequency="Daily")
    evening_task = Task(title="Evening Check", description="Quick evening check", time="14:00", frequency="Daily")
    snack_task = Task(title="Snack Time", description="Give a small treat", time="19:00", frequency="Daily")
    duplicate_task = Task(title="Morning Medicine", description="Give medicine", time="09:00", frequency="Daily")

    mochi.add_task(walk_task)
    mochi.add_task(feed_task)
    mochi.add_task(evening_task)
    mochi.add_task(duplicate_task)
    luna.add_task(play_task)
    luna.add_task(litter_task)
    luna.add_task(snack_task)

    scheduler = Scheduler(scheduler_id="scheduler-1")
    tasks = [walk_task, feed_task, play_task, litter_task, evening_task, snack_task, duplicate_task]

    print("\nTest 1: sort_by_time()")
    print("-" * 40)
    sorted_tasks = scheduler.sort_by_time(tasks)
    for task in sorted_tasks:
        pet_name = task.pet.name if task.pet else "Unknown"
        print(f"{task.time} | {pet_name} | {task.title}")
    print("-" * 40)

    print("\nTest 2: filter_tasks() - uncompleted tasks")
    print("-" * 40)
    pending_tasks = scheduler.filter_tasks(tasks, status=False)
    for task in pending_tasks:
        pet_name = task.pet.name if task.pet else "Unknown"
        print(f"{task.time} | {pet_name} | {task.title} | Pending")
    print("-" * 40)

    print("\nTest 3: filter_tasks() - tasks for one pet")
    print("-" * 40)
    mochi_tasks = scheduler.filter_tasks(tasks, pet_name="Mochi")
    for task in mochi_tasks:
        print(f"{task.time} | Mochi | {task.title}")
    print("-" * 40)

    conflict_warning = scheduler.check_conflicts(tasks)
    print("\nTest 4: check_conflicts()")
    print("-" * 40)
    if conflict_warning:
        print(conflict_warning)
    else:
        print("No conflicts detected.")
    print("-" * 40)

    print("\nToday's Schedule")
    print("-" * 40)
    print(f"{'Pet':<10} {'Time':<8} {'Task':<20} {'Status':<8}")
    print("-" * 40)
    schedule = scheduler.compile_tasks_for_owner(owner)
    for task in schedule:
        pet_name = task.pet.name if task.pet else "Unknown"
        status = "Done" if task.completion_status else "Pending"
        print(f"{pet_name:<10} {task.time:<8} {task.title:<20} {status:<8}")
    print("-" * 40)


if __name__ == "__main__":
    main()
