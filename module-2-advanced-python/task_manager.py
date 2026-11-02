class Task:
    """Represents a single task with a title, priority, and completion status."""

    # Class variable - shared across all instances
    VALID_PRIORITIES = ["low", "medium", "high"]

    def __init__(self, title, priority="medium"):
        self.title = title
        self.completed = False  # All tasks start incomplete

        # Validate priority before setting it
        if priority.lower() not in self.VALID_PRIORITIES:
            raise ValueError(f"Priority must be one of {self.VALID_PRIORITIES}")
        self.priority = priority.lower()

    def complete(self):
        """Mark the task as completed."""
        self.completed = True
    def __repr__(self):
        """Return a string representation of the task."""
        status = "Completed" if self.completed else "Incomplete"
        return f"Task(title='{self.title}', priority='{self.priority}', status='{status}')"
#quick test
# task1 = Task("Learn OOP", "high")
# task2 = Task("Write unit tests")

# print(task1)
# print(task2)

# task1.complete()
# print(task1)

# bad_task = Task("do something", "urgent")
# 
class TaskManager:
    """Manages a collection of tasks."""

    def __init__(self):
        self.tasks = []

    def add_task(self, title, priority):
        task = Task(title, priority)
        self.tasks.append(task)
        return task
    def complete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                task.complete()
                return True
        return False
    def get_pending(self):
        return [task for task in self.tasks if task.completed]

    def get_by_priority(self, priority):
        return [ task for task in self.tasks if task.priority == priority]
    def summary(self):
        total = len(self.tasks)
        done = sum(1 for task in self.tasks if task.complete())
        print(f'\n Task Summary: {done}/{total} completed')
        for task in self.tasks:
            print(f'  {task}')
#full test

manager = TaskManager()
manager.add_task('Set up virtual env', 'high')
manager.add_task('read big o lesson', 'high')
manager.add_task('practice linked list', 'medium')
manager.add_task('review strech excercise', 'low')

manager.complete_task('Set up virtual env')
manager.complete_task('read big o lesson')

manager.summary()