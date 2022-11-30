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
<IP>:<PORT>/create/
```

List of apps

```
<IP>:<PORT>/apps/
```

Detail of app

```
<IP>:<PORT>/apps/ID/
```

Update app

```
<IP>:<PORT>/apps/ID/update
```

Delete app

```
<IP>:<PORT>/apps/ID/delete
```

Run app

```
<IP>:<PORT>/apps/ID/run
```

List of runs

```
<IP>:<PORT>/run/
```
