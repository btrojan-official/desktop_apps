from datetime import datetime

class Task():
    def __init__(self, title: str, status: str, due_date: datetime|str):
        self.title = title
        self.status = status
        
        self.date_format = "%Y-%m-%d %H:%M:%S"
        self.due_date = due_date if type(due_date) != str else datetime.strptime(due_date, self.date_format)
        
    def is_past_due(self):
        return self.due_date < datetime.now()
    
    def __str__(self):
        return f"{self.title} || {self.status} || {self.due_date.strftime(self.date_format)}"
    
    def to_dict(self):
        return {
            "title": self.title,
            "status": self.status,
            "due_date": self.due_date.strftime(self.date_format)
        }