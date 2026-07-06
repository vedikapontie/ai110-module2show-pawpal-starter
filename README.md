# PawPal+ (Module 2 Project)

You are building **PawPal+**, a Streamlit app that helps a pet owner plan care tasks for their pet.

## Scenario

A busy pet owner needs help staying consistent with pet care. They want an assistant that can:

- Track pet care tasks (walks, feeding, meds, enrichment, grooming, etc.)
- Consider constraints (time available, priority, owner preferences)
- Produce a daily plan and explain why it chose that plan

Your job is to design the system first (UML), then implement the logic in Python, then connect it to the Streamlit UI.

## What you will build

Your final app should:

- Let a user enter basic owner + pet info
- Let a user add/edit tasks (duration + priority at minimum)
- Generate a daily schedule/plan based on constraints and priorities
- Display the plan clearly (and ideally explain the reasoning)
- Include tests for the most important scheduling behaviors

## Getting started

### Setup

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### Suggested workflow

1. Read the scenario carefully and identify requirements and edge cases.
2. Draft a UML diagram (classes, attributes, methods, relationships).
3. Convert UML into Python class stubs (no logic yet).
4. Implement scheduling logic in small increments.
5. Add tests to verify key behaviors.
6. Connect your logic to the Streamlit UI in `app.py`.
7. Refine UML so it matches what you actually built.

## 🖥️ Sample Output

Today's Schedule
----------------------------------------
Pet        Time     Task                 Status  
----------------------------------------
Mochi      07:30    Morning Walk         Pending 
Mochi      08:00    Feed Breakfast       Pending 
Luna       18:00    Play Session         Pending 
Luna       20:00    Clean Litter Box     Pending 
----------------------------------------

## 🧪 Testing PawPal+

```bash
# Run the full test suite:
pytest

# Run with coverage:
pytest --cov
```

The PawPal+ test validates the core scheduling behaviors of the backend logic using pytest. It verifies sorting correctness, daily task reoccurence, and checks for duplicate tasks. 

Sample test output:

```
python -m pytest

# Paste your pytest output here
```
================================== test session starts ==================================
platform win32 -- Python 3.13.13, pytest-9.0.3, pluggy-1.6.0
rootdir: C:\Users\vedik\Documents\GitHub\ai110-module2show-pawpal-starter
plugins: anyio-4.13.0
collected 3 items                                                                        

tests\test_pawpal.py ...                                                           [100%]

=================================== 3 passed in 0.07s ===================================


Confidence Level: 4 stars


## 📐 Smarter Scheduling

The scheduler now includes a small set of smart behaviors to keep pet care plans practical and easy to manage.

- Sorting behavior: Scheduler.sort_by_time() orders tasks by their HH:MM time values for a clear daily sequence.
- Filtering behavior: Scheduler.filter_tasks() helps isolate tasks by pet name or completion status.
- Conflict detection: Scheduler.check_conflicts() warns when multiple tasks share the same time slot.
- Recurring task logic: recurring Daily and Weekly tasks generate the next occurrence automatically when marked complete.

## 📸 Demo Walkthrough

Describe your app in numbered steps so a reader can follow along without watching a video:

1. <!-- Describe this step --> Add pet name and information
2. <!-- Describe this step --> Schedule tasks for the pet of your choice at the designated times and select priority
3. <!-- Describe this step --> Add task to scheduler
4. <!-- Describe this step --> View scheduler for the plan of the day
5. <!-- Add more steps as needed --> After completing a task press task completed
6. There will be warnings if more than one task is scheduled at the same time

----------------------------------------
Mochi      07:30    Morning Walk         Pending 
Mochi      08:00    Feed Breakfast       Pending 
Mochi      09:00    Morning Medicine     Pending 
Mochi      14:00    Evening Check        Pending 
Luna       18:00    Play Session         Pending 
Luna       19:00    Snack Time           Pending 
Luna       20:00    Clean Litter Box     Pending 
----------------------------------------

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or link to a demo video here -->
