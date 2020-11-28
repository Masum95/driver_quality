
# driver_quality
A django based program that gives drivers' feedback according to their completion rate. 

For design-documentation, please refer to **Design.pdf**

## Basic Project Structure 

```
root
├── driver_quality
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── supply_order -->(Module containing data model & logic) 
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py  
│   ├── enums.py    -->( StatusChoices) 
│   ├── models.py   -->( Contains model table ) 
│   ├── pagination.py  -->( Custom pagination class ) 
│   ├── querysets.py   -->( Queryset class for filtering ) 
│   ├── serializers.py  
│   ├── tests.py    -->( Unit testing ) 
│   ├── urls.py    -->(URL Resolver ) 
│   └── views.py   -->( Contains the actual Logic ) 
├── .env   -->( environment file for docker ) 
├── .gitignore
├── docker-compose.yml  
├── Dockerfile
├── manage.py 
├── README.md
├── requirements.txt
├── resetmigrations.sh  
├── run.sh  -->( Run this script to up the backend server)
├── seeder.py  -->(Python script for inserting dummy data)
└── client.py -->( Client Program to test server ) 
└── Design.pdf -->( Client Program to test server ) 

```

## How to Run
---

### To build and run using docker:

Following section assumes you have docker installed on your machine.

Running the **run.sh** script builds the docker image , does necessary django migrations, inserts dummy data and then runs the django dev server @8000 port. Postgres-db port is mapped to **5454** port of localhost. 
 
To run the script, use the command from terminal:

> ./run.sh

To learn the distribution of dummy dataset, Please refer to **Design.pdf**

As client program, a simple python program called
**client.py** is used. 
This program continuously takes driver id as input from the user ( until ***q*** is pressed ) and gives corresponding completion rate and message on the terminal. 

To run the program use 

> python3 client.py


