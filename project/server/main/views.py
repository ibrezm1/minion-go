# project/server/main/views.py

from celery.result import AsyncResult
from flask import render_template, Blueprint, jsonify, request


from project.server.tasks import create_bound_task
from project.server.tasks import fail_bound_task
from project.server.tasks import create_bound_plugin
from project.server.tasks import create_filtered_bound_plugin

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

@main_blueprint.route("/tasksp", methods=["POST"])
def run_taskp():
    content = request.json
    task_type = content["type"]
    task = create_bound_plugin.delay(int(task_type))
    #task = create_bound_plugin.apply_async(args=(int(task_type)), countdown=2)
    return jsonify({"task_id": task.id}), 202

# https://stackoverflow.com/questions/11672179/setting-time-limit-on-specific-task-with-celery
# https://docs.celeryproject.org/en/stable/userguide/tasks.html
@main_blueprint.route("/taskspa", methods=["POST"])
def run_taskpa():
    content = request.json
    task_type = content["type"]
    #task = create_bound_plugin.delay(int(task_type))
    task = create_bound_plugin.apply_async(args=[17],\
                                    countdown=2,time_limit=15, \
                                    soft_time_limit=10,
                                    retry=True, retry_policy={
                                                    'max_retries': 3,
                                                    'interval_start': 0,
                                                    'interval_step': 0.2,
                                                    'interval_max': 0.2,
                                                }
                                    )
    return jsonify({"task_id": task.id}), 202


@main_blueprint.route("/taskspaf", methods=["POST"])
def run_taskpaf():
    content = request.json
    #task_type = content["ucname"]
    #task = create_bound_plugin.delay(int(task_type))
    task = create_filtered_bound_plugin.apply_async(args=[0],\
                                    kwargs= content,\
                                    countdown=2,time_limit=15, \
                                    soft_time_limit=10,
                                    retry=True, retry_policy={
                                                    'max_retries': 3,
                                                    'interval_start': 0,
                                                    'interval_step': 0.2,
                                                    'interval_max': 0.2,
                                                }
                                    )
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

