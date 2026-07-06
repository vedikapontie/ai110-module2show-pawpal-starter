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

    mochi.add_task(walk_task)
    mochi.add_task(feed_task)
    luna.add_task(play_task)
    luna.add_task(litter_task)

    scheduler = Scheduler(scheduler_id="scheduler-1")
    schedule = scheduler.compile_tasks_for_owner(owner)

    print("\nToday's Schedule")
    print("-" * 40)
    print(f"{'Pet':<10} {'Time':<8} {'Task':<20} {'Status':<8}")
    print("-" * 40)
    for task in schedule:
        pet_name = task.pet.name if task.pet else "Unknown"
        status = "Done" if task.completion_status else "Pending"
        print(f"{pet_name:<10} {task.time:<8} {task.title:<20} {status:<8}")
    print("-" * 40)


if __name__ == "__main__":
    main()
