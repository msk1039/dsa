class TaskNode:
    def __init__(self, description, priority):
        self.description = description
        self.priority = priority
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, description, priority):
        new_task = TaskNode(description, priority)
        new_task.next = self.top
        self.top = new_task

    def pop(self):
        if self.top is None:
            return None
        removed_task = self.top
        self.top = self.top.next
        return removed_task

    def display_task_by_priority(self):
        priorities = {"High": [], "Medium": [], "Low": []}
        current = self.top
        while current:
            priorities[current.priority].append(current.description)
            current = current.next
        for priority, tasks in priorities.items():
            if tasks:
                print(f"Tasks With {priority} Priority")
                for task in tasks:
                    print(f"   -Task : {task}")


# Example usage
stack = Stack()
stack.push("Task 1", "High")
stack.push("Task 2", "Medium")
stack.push("Task 3", "Low")

print("Tasks in stack:")
stack.display_task_by_priority()

print("\nRemoving top task...")
stack.pop()

print("Tasks in stack after removal:")
stack.display_task_by_priority()