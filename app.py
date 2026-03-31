class TodoService:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def create_task(self, title, description=""):
        if not title:
            raise ValueError("Title is required")
        task = {
            "id": self.next_id,
            "title": title,
            "description": description,
            "status": "pending",
            "priority": "medium"
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self):
        return self.tasks

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks.pop(i)
                return True
        return False
