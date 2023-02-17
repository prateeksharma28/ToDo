from app.models import Task





def validate_add_task_request(data):
    if not data:
        return False
    if not data.get("name"):
        return False
    if type(data.get("name")) is int:
        return False

    return True


def validate_update_task_request(data):
    if not data:
        return False
    if not (data.get("id") or data.get("name") or data.get("status")):
        return False
    if type(data.get("id")) is not int:
        return False
    if type(data.get("name")) is int:
        return False
    if type(data.get("status")) is not bool:
        return False
    task_id = data.get("id")
    task = Task.query.get(task_id)
    if not task:
        return False

    return True


def validate_delete_task_request(data):
    if not data:
        return False
    if not data.get("id"):
        return False
    if type(data.get("id")) is not int:
        return False
    task_id = data.get("id")
    task = Task.query.get(task_id)
    if not task:
        return False

    return True

