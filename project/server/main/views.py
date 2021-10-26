# project/server/main/views.py

from celery.result import AsyncResult
from flask import render_template, Blueprint, jsonify, request


from project.server.tasks import create_bound_task
from project.server.tasks import fail_bound_task

from flask import Flask, make_response

main_blueprint = Blueprint("main", __name__,)

def cleanStr(to_clean):
    to_clean = str(to_clean)
    clean_items = ['"',"'","\\"]
    for cleanit in clean_items:
        to_clean = to_clean.replace(cleanit,"")
    return to_clean

@main_blueprint.route("/", methods=["GET"])
def home():
    return render_template("main/home.html")


@main_blueprint.route("/tasksb", methods=["POST"])
def run_task2():
    content = request.json
    task_type = content["type"]
    task = create_bound_task.delay(int(task_type))
    return jsonify({"task_id": task.id}), 202

@main_blueprint.route("/tasksf", methods=["POST"])
def run_task3():
    content = request.json
    task_type = content["type"]
    task = fail_bound_task.delay(int(task_type))
    return jsonify({"task_id": task.id}), 202

@main_blueprint.route("/tasksb/<task_id>", methods=["GET"])
def get_status2(task_id):
    task_result = AsyncResult(task_id)
    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": cleanStr(task_result.result),
        "task_info": cleanStr(task_result.info)
    }
    return jsonify(result), 200

