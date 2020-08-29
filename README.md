# Weather_app

Python api which send json(Weather_data) output if current date(day) is prime if current date(day) is not prime then api will send "Date is not prime so no data"
## Setup
```bash
pip install -r requirements.txt
```
```bash
python manage.py migrate
```
```bash
python manage.py createsuperuser
```
## Launch app - 
```bash
python manage.py runserver
```


## Apis
```bash
http://127.0.0.1:8000/api #Check Prime day
```
```bash
http://127.0.0.1:8000/admin #admin panel to check stored data
```
