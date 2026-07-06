# PawPal+ Project Reflection

## 1. System Design
Three core actions that a user should be able to perform:
1. enter the user and pet information
2. add and edit pet care tasks such as a walk or doctor appointmet or grooming
3. access, view, and edit schedule

**a. Initial design**

- Briefly describe your initial UML design.
- What classes did you include, and what responsibilities did you assign to each?

Based on the requirements, the initial UML design works around the four core classes in an optimal manner for scheduling coordination. The four classes that were used were Owner, Pet, Task, and Scheduler. The Owner class manages the user's profile information and has the access to the pet, essentially a container for the Pet objects. The Pet class has a data object which tracks the pets' information such as its name, species, and age. It also is the owner/manager of the tasks. The Task class has to hold the scheduled time, keep track of the description, amount of time, priority, and if the task has been completed. Finally, the schedule is the central brain which handles the operations, figuring out needs based on the pet/s, sorting chronologically based on times and priority, and detecting time conflicts. 

**b. Design changes**

- Did your design change during implementation?
- If yes, describe at least one change and why you made it.

Yes I made a design change during implementation, there was a lack of the Pet being linked back to the Owner, I made sure to add that line of code just to have a way to cross check the relationship. Additionally, if there are multiple pets I also added a link from the Task to the Pet. 

---

## 2. Scheduling Logic and Tradeoffs

**a. Constraints and priorities**

- What constraints does your scheduler consider (for example: time, priority, preferences)?
- How did you decide which constraints mattered most?

**b. Tradeoffs**

- Describe one tradeoff your scheduler makes.
- Why is that tradeoff reasonable for this scenario?

I made the scheduler check for conflicts by looking at the tasks that have the same starting time; however, it does not check how long a task takes. I believe that this tradeoff is reasonable because it allows the code to run simply without needing complex math. Although the user has to check for these it is fine because the schedule manager makes it clear when the next activity starts. I would like to implement this possibly in the future. 

---

## 3. AI Collaboration

**a. How you used AI**

- How did you use AI tools during this project (for example: design brainstorming, debugging, refactoring)?
- What kinds of prompts or questions were most helpful?

**b. Judgment and verification**

- Describe one moment where you did not accept an AI suggestion as-is.
- How did you evaluate or verify what the AI suggested?

---

## 4. Testing and Verification

**a. What you tested**

- What behaviors did you test?
- Why were these tests important?

**b. Confidence**

- How confident are you that your scheduler works correctly?
- What edge cases would you test next if you had more time?

---

## 5. Reflection

**a. What went well**

- What part of this project are you most satisfied with?

**b. What you would improve**

- If you had another iteration, what would you improve or redesign?

**c. Key takeaway**

- What is one important thing you learned about designing systems or working with AI on this project?
