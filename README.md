# Minion Go - Dynamic Task creation and fulfillment Tracker

Built out of frustration to do mundane IT tasks on a recurring basis!! Some times you just want to handover a python file to someone and ask him to run this regularly at XX time of the day to send out the report or perform healthcheck. 
While other times if an issue or incident comes you should be able to ask someone to run the python file and get it resolved.

These are the two major usecases for this project.

## Want to use this project?

Spin up the containers:

```sh
docker-compose up -d --build
docker-compose up -d --build --force-recreate
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

Running the app <br/>
Run sudo rabbitmq-server<br/>
Run celery -A app.celery worker --loglevel=INFO --pidfile='' in another terminal window.<br/>
Run celery -A app.celery beat --loglevel=INFO --pidfile='' in yet another terminal.<br/>
Finally, run flask run and the website should be up on: http://127.0.0.1:5000/<br/>

Swarm<br/>
https://docs.docker.com/engine/swarm/stack-deploy/<br/>
https://labs.play-with-docker.com/ __
https://stackoverflow.com/questions/5544629/retrieve-list-of-tasks-in-a-queue-in-celery

## Need Lookups ?

* [Flask and celery](https://testdriven.io/blog/flask-and-celery/).
* I keep forgeting [Markup in git](https://github.com/tchapi/markdown-cheatsheet/blob/master/README.md)
* Notes on [Celery states](https://www.distributedpython.com/2018/09/28/celery-task-states/)

## TODO items decreasing priority
- [x] Implement plugin framework for usecase identification
- [x] Task states and failures
- [x] Update versions of flower and celery
- [ ] Implement variables pickup - from request > loadjson
- [ ] Store all tasks state changes
- [ ] Update Readme with setup details see [here](https://awesomeopensource.com/projects/celery)
- [ ] Add Docker swarm steps in readme
- [ ] Add requirements.txt for usecases and load in the file
- [ ] guinicorn or waitress inplace of flask default
- [ ] remove hacky tone (prints and temp routes etc)
- [ ] Change the react UI that is useless
- [ ] Mention the githubs I scanned for code

## Ponder over 
1. Do we need seconday loadjson at a master level ? 
2. Do we need better UI in place if useless one
3. Do we need [rabitmq](https://github.com/delivey/flask-celery-rabbitmq-code)
4. Do we need Django in place of flask , why ? 
