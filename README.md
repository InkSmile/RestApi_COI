## Installation

If you want to install this project on your computer you need to copy this project

```bash
git clone https://github.com/InkSmile/Junior-FullStack-project.git
```
Then you need to install [Docker](https://docs.docker.com/engine/install/)

Run command

```bash
docker-compose up --build
```

Wait until docker buil your project. In your browser enter url http://0.0.0.0:8000

If docker does not work for some reason you can install the project manually

First, create virtual enviroment

```bash
python -m venv venv
```
or
```bash
python3 -m venv venv
```
Activate for Linux
```bash
source venv/bin/activate 
```

Then install all packages
```bash
pip install -r requirements.txt
```
**_NOTE:_**   You need to change .env file depending on what your database credentials is

Make migrations
```bash
python manage.py makemigrations
```
Migrate to database
```bash
python manage.py migrate
```
Create super user
```bash
python manage.py createsuperuser
```
Run server
```bash
python manage.py runserver
```
**_NOTE:_**  ''python'' command may not work on your machine, if it is try -  ''python3''



# API Endpoints

http://127.0.0.1:8000/api/directions/ - return all directions

<br/>http://127.0.0.1:8000/api/doctors/?work_experience__gte=20 - filter doctors with work experience greater than 20 years

<br/> http://127.0.0.1:8000/api/doctors/?ordering=data_of_birthday - data of birthday ordering

<br/> http://127.0.0.1:8000/api/doctors/?ordering=work_experience - work experience ordering