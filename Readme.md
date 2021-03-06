### django-erp
A django ERP system which keeps Customer, Product, Order and Payments data.

### Database Settings
Create an .env file and add these parameters for your Postgresql DB. 
```markdown
DB_NAME="..."
DB_USER="..."
DB_PASSWORD="..."
DB_HOST="..."
DB_PORT="5432"
```
and add also
```
DEBUG=True
SECRET_KEY="your secret key"
```

### Run Server
`sudo service postgresql restart`
`source ../venv/bin/activate`
`python3 manage.py runserver`

### Commands
**Start Database serice**
`sudo service postgresql restart`

**Create Virtual Enviroment**
`virtualenv venv`

**activate venv**
`source ../venv/bin/activate`

**start project**
`django-admin startproject product`

**migrate tables**
`python3 manage.py migrate`

**Run Server**
`python3 manage.py runserver`

**create super user**
`python3 manage.py createsuperuser`

**create a new application**
`python3 manage.py startapp appname`

**make migrations**
`python3 manage.py makemigrations`

**run shell**
`python3 manage.py shell`

**generate dependencies**
`pip freeze > requirements.txt`

**Models CASCADE or ...**
`CASCADE` : When the referenced object is deleted, also delete the objects that have references to it (when you remove a blog post for instance, you might want to delete comments as well). SQL equivalent: CASCADE.
`PROTECT` Forbid the deletion of the referenced object. To delete it you will have to delete all objects that reference it manually. SQL equivalent: RESTRICT.
`RESTRICT`: (introduced in Django 3.1) Similar behavior as PROTECT that matches SQL's RESTRICT more accurately. (See django documentation example)
`SET_NULL` : Set the reference to NULL (requires the field to be nullable). For instance, when you delete a User, you might want to keep the comments he posted on blog posts, but say it was posted by an anonymous (or deleted) user. SQL equivalent: SET NULL.
`SET_DEFAULT` : Set the default value. SQL equivalent: SET DEFAULT.
`SET(...)` : Set a given value. This one is not part of the SQL standard and is entirely handled by Django.
`DO_NOTHING` : Probably a very bad idea since this would create integrity issues in your database (referencing an object that actually doesn't exist). SQL equivalent: NO ACTION. 

**Change Password**
`python3 manage.py changepassword <user_name>`

### APIs

#### POST Requests

**New Product**
***http://localhost:8000/products/api***
```json
{
  "name": "Product-18",
  "is_active": true,
  "images": [
    "4b0ccb54-6406-42ea-8ee7-7a2d89ae70d5",
    "db47c6ea-29cd-4369-8668-d054ae3875f2"
  ],
  "description": "??effaf afsg",
  "price": 4.25,
  "stock": 8000
}
```

***New Order***
***http://localhost:8000/orders/api***
```json
{
  "customer": "162eeb12-eff1-4fea-bd96-a0a56c2b461e",
  "items": [
    "738b4f78-4766-418d-8013-766018e9755b",
    "17ea292f-775d-440a-8c01-896c847ee266"
  ],
  "status": "CP",
  "note": "scas"
}
```

**New Customer**
***http://localhost:8000/customers/api***
```json
{
  "name": "ABC Inc.",
  "person": "Hereweald Endre",
  "taxnumber": "3252352323",
  "address": "2257 Wandering Ln Brea, California(CA), 92821",
  "telephone": "(714) 255-8378",
  "email": "asdasf@asf.com",
  "bankAccount": "89768584925839454"
}

```

#### PUT, DELETE Requests
**Order**
***http://localhost:8000/orders/api/[id]*** 
**Customer**
***http://localhost:8000/customers/api/[id]*** 
**Product**
***http://localhost:8000/products/api/[id]*** 