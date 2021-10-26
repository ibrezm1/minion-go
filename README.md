# Asynchronous Tasks with Flask and Celery

Example of how to handle background processes with Flask, Celery, and Docker.

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/flask-and-celery/).

## Want to use this project?

Spin up the containers:

```sh
$ docker-compose up -d --build
```

Open your browser to [http://localhost:5004](http://localhost:5004) to view the app or to [http://localhost:5556](http://localhost:5556) to view the Flower dashboard.

Trigger a new task:

```sh
$ curl http://localhost:5004/tasks -H "Content-Type: application/json" --data '{"type": 0}'
```

Check the status:

```sh
$ curl http://localhost:5004/tasks/<TASK_ID>
$ curl http://localhost:5004/tasks/8bb507cb-2b12-4b5f-b006-ef5fe8b8ff29
```


Todo :
https://www.distributedpython.com/2018/09/28/celery-task-states/

https://stackoverflow.com/questions/21885814/how-to-iterate-through-a-modules-functions