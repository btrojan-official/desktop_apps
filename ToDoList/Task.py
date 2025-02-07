from datetime import datetime

class Task():
    def __init__(self, title: str, status: str, due_date: datetime):
        self.title = title
        self.status = status
        self.due_date = due_date
        
    def is_past_due(self):
        return self.due_date < datetime.now()
    
    def __str__(self):
        return f"{self.title} || {self.status} || {self.due_date.strftime("%Y-%m-%d %H:%M")}"