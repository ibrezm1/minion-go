# Minion Go - Dynamic Task creation and fulfillment Tracker

Built out of frustration to do mundane IT tasks on a recurring basis!! Some times you just want to handover a python file to someone and ask him to run this regularly at XX time of the day to send out the report or perform healthcheck. 
While other times if an issue or incident comes you should be able to ask someone to run the python file and get it resolved.

These are the two major usecases for this project.

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

https://github.com/delivey/flask-celery-rabbitmq-code

Running the app <br/>
Run sudo rabbitmq-server<br/>
Run celery -A app.celery worker --loglevel=INFO --pidfile='' in another terminal window.<br/>
Run celery -A app.celery beat --loglevel=INFO --pidfile='' in yet another terminal.<br/>
Finally, run flask run and the website should be up on: http://127.0.0.1:5000/<br/>

Swarm<br/>
https://docs.docker.com/engine/swarm/stack-deploy/<br/>
https://labs.play-with-docker.com/ __
https://stackoverflow.com/questions/5544629/retrieve-list-of-tasks-in-a-queue-in-celery

## Want to learn how to build this?

Check out the [post](https://testdriven.io/blog/flask-and-celery/).

