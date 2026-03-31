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
            "status": "pending"
        }
        self.tasks.append(task)
        self.next_id += 1
        return task

    def get_all_tasks(self):
        return self.tasks

    def get_task_by_id(self, task_id):
        for task in self.tasks:
            if task["id"] == task_id:
                return task
        return None

    def update_task(self, task_id, data):
        task = self.get_task_by_id(task_id)
        if not task:
            return None
        task.update(data)
        return task

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task["id"] == task_id:
                self.tasks.pop(i)
                return True
        return False
class TaskNotificationService:
    """Service de notifications pour les tâches."""
    def notify(self, task: dict, event: str) -> str:
        message = f"[{event.upper()}] Tâche #{task['id']}: {task['title']}"
        print(message)
        return message
