# Hamravesh-Task
Django restful platform for running docker containers. <br>
[Docker SDK](https://docker-py.readthedocs.io/en/stable/containers.html#) is used for the run part.

## Run

```
git clone https://github.com/mo1ein/Hamravesh-Task.git
cd Hamravesh-Task
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

## Endpoints

Create app

```
localhost:8000/create/
```

List of apps

```
localhost:8000/apps
```

Detail of app

```
localhost:8000/apps/ID/
```

Update app

```
localhost:8000/apps/ID/update
```

Delete app

```
localhost:8000/apps/ID/delete
```

Run app

```
localhost:8000/apps/ID/run
```

List of runs

```
localhost:8000/run/
```
