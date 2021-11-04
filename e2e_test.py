import requests
import time
ploads = {"type": 1}
r = requests.post('http://localhost:5004/tasksb',json=ploads)
task_id = r.json()['task_id']
print(task_id)
time.sleep(2)
r = requests.get(f'http://localhost:5004/tasksb/{task_id}')
print(r.json())

r = requests.post('http://localhost:5004/tasksf',json=ploads)
task_id = r.json()['task_id']
print(task_id)
time.sleep(2)
r = requests.get(f'http://localhost:5004/tasksb/{task_id}')
print(r.json())


r = requests.post('http://localhost:5004/tasksp',json=ploads)
task_id = r.json()['task_id']
print(task_id)
time.sleep(2)
r = requests.get(f'http://localhost:5004/tasksb/{task_id}')
print(r.json())

r = requests.post('http://localhost:5004/taskspa',json=ploads)
task_id = r.json()['task_id']
print(task_id)
time.sleep(3)
r = requests.get(f'http://localhost:5004/tasksb/{task_id}')
print(r.json())
time.sleep(15)
r = requests.get(f'http://localhost:5004/tasksb/{task_id}')
print(r.json())

r = requests.get(f'http://localhost:5556/api/tasks')
tot = len(r.json())
print(tot)

assert tot != 0,"No requests were fired"


r = requests.post('http://localhost:5004/taskspaf',json={'ucname':'CustomLoad','time':5})
task_id = r.json()['task_id']
print(task_id)
time.sleep(2)
r = requests.get(f'http://localhost:5004/tasksb/{task_id}')
print(r.json())
time.sleep(2)
r = requests.get(f'http://localhost:5004/tasksb/{task_id}')
print(r.json())