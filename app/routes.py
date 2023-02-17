from app import app, db
from app.models import Task
from flask import request
from app.helper import validate_add_task_request, validate_delete_task_request, validate_update_task_request


@app.route('/task', methods=['GET'])
def list_tasks():
    tasks = Task.query.all()
    return {
        "status":"success", 
        "tasks": [{
            "task_id":task.id,
            "name":task.content,
            "status":task.done
        } for task in tasks]
    }


@app.route('/task', methods=['POST'])
def add_task():
    body = request.json
    if not validate_add_task_request(body):
        return {
            "status":"fail"
        }, 400
    task_name = body.get("name")
    task = Task(task_name)
    db.session.add(task)
    db.session.commit()
    return {"status":"success"}

@app.route('/task', methods=['PUT'])
def update_task():
    body = request.json
    if not validate_update_task_request(body):
        return {
            "status":"fail"
        }, 400
    task_id = body.get("id")
    edit_text = body.get("name")
    status = body.get("status")
    task = Task.query.get(task_id)
    task.content = edit_text
    if status:
        task.done = True
    else:
        task.done = False
    db.session.commit()
    return ({
        "status":"success"
    })


@app.route('/task', methods=['DELETE'])
def delete_task():
    body = request.json
    if not validate_delete_task_request(body):
        return {
            "status":"fail"
        }, 400
    task_id = body.get("id")
    task = Task.query.get(task_id)
    db.session.delete(task)
    db.session.commit()
    return ({
        "status":"success"
    })
