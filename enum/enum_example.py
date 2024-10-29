from enum import Enum

class Status(Enum):
    PENDING = 1
    IN_PROGRESS = 2
    COMPLETED = 3   
    FAILED = 4

def check_status(status):
    if status == Status.COMPLETED:
        print("Task is completed!")
    elif status == Status.PENDING:
        print("Task is still pending.")

check_status(Status.PENDING)  # Output: Task is completed!
