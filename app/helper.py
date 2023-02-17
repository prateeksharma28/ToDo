from app.models import Task
'''
this helps in checking a few edge cases
'''




def validate_add_task_request(data):
    # empty request
    if not data:
        return False
    # task name not given
    if not data.get("name"):
        return False
    # wrong format of task's title given
    if type(data.get("name")) is int:
        return False

    return True


def validate_update_task_request(data):
    # empty request
    if not data:
        return False
    # task data not given
    if not (data.get("id") or data.get("name") or data.get("status")):
        return False
    # wrong format of task's id given
    if type(data.get("id")) is not int:
        return False
    # wrong format of task's title given
    if type(data.get("name")) is int:
        return False
    # wrong format of task's status given
    if type(data.get("status")) is not bool:
        return False
    # if task id not present in database
    task_id = data.get("id")
    task = Task.query.get(task_id)
    if not task:
        return False

    return True


def validate_delete_task_request(data):
    # empty request
    if not data:
        return False
    # task's id not given
    if not data.get("id"):
        return False
    # wrong format of task's id given
    if type(data.get("id")) is not int:
        return False
    # if task id not present in database
    task_id = data.get("id")
    task = Task.query.get(task_id)
    if not task:
        return False

    return True

