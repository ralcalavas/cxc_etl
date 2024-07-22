# cxc_etl
ETL to transform data into CXC

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Clone the repository
```
git clone git@github.com:ralcalavas/cxc_etl.git
```

### Prerequisites

- python Use: v3.12.4
- django Use: v5.0.7
- pip

```
$ python -m ensurepip --upgrade
```

##### Dockers

* PosgreSQL
```
docker run -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=pass -p 5432:5432 -d postgres
``` 

### Installing

To install the dependencies you have to execute the following commands, port by default is 80.
 
1. Install requirements
    ```
    pip install -r requirements.txt
    ```
2. Copy env.example file to .env. Consider docker variables to build the env
    ```
    $ cp .env.example .env
    ```
3. Run migrations
    ```
    python manage.py migrate
    ```
4. Run server
   ```
   python manage.py runserver
   ```

## Running the tests

```
python manage.py test
```

## Running app

1. Charge catalog data
    ```
    curl --location --request GET 'http://127.0.0.1:8000/employees/charge_catalog'
    ```
2. Charge employees data
    ```
    curl --location --request GET 'http://127.0.0.1:8000/employees/charge_employees'

## Built With

* [Postgresql](https://www.postgresql.org/) - Relational Database used
* [Django](https://www.djangoproject.com/start/) - The python framework used

## Contributing

* **Ricardo Alcala Vasquez** - ricardo.alcala1@gmail.com