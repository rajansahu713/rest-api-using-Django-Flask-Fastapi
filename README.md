## RestApi using Django, Flask and Fastapi

I have created CRUD operation restfull API using Django, Flask and FastApi.
All the above frameworks are Python web-framwework. Lets discuss one by one


#### Django rest framwork
    REST APIs are an industry-standard way for web services to send and receive data. They use HTTP request methods to facilitate the request-response cycle and typically transfer   data using JSON, and more rarely - HTML, XML and other formats
  
#### Flask 
    Flask is a popular micro framework for building web applications. Since it is a micro-framework, it is very easy to use and lacks most of the advanced functionality which is found in a full-fledged framework.
  
#### FastApi
    FastAPI is a modern, python-based high-performance web framework used to create Rest APIs. Its key features are that is fast, up to 300% faster to code, fewer bugs, easy to use, and production-friendly.
  
### Camparision between Django, Flask and FastApi

1. <h4>Packages</h4>
    Among Django, Flask, and FastAPI, Django has the most packages that enable reusability of code. It is a full-stack web development framework, unlike Flask and FastAPI, that are minimalistic frameworks used for building fast websites.
2. <h4>Community</h4>
    Django has the most significant community because of its wide use and popularity next to Flask, which also has a thriving community. FastAPI, on the other hand, has a small community because it’s relatively new.

3. <h4>Performance</h4>
    In performance, FastAPI is the leader because it is speed-oriented, then next to Flask, and finally Django, which is not very fast.

4. <h4>Flexibility</h4>
    Flexibility is something developers value a lot, and Flask is more flexible than Django. Fast API, on the other hand, is flexible code-wise and doesn’t restrict the code layout. So we can say Flask is the most flexible among all three.

Lets have look at code how to build Crud in different framework:
 
Django

Requirement  
```python
pip install django
pip install djangorestframework
```
Install all the above packages

Step 1:
  After installing the package mentioned above 
  ```
  django-admin startproject app #app is project name
  ```
Step 2:
  ```
  python manage.py startapp fn_api #fn_api is app name
  ```


The structure of file look like this
<br>
<img align="center" src="https://github.com/rajansahu713/rest-api-using-Django-Flask-Fastapi/blob/main/images/django.png" width="250" height="350">
  
Step 3
    Registor the app -> Go to setting file in INSTALLED_APPS section mention app name
 
 ```python
    INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'fn_api',
```
Step 4:
    Create models and Serializer
    
```python
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="") 

    def __str__(self):
        return self.product_name
        
```

Serializer
```python
from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('product_id', 'product_name', 'category')
```

Step 5:
    we need to write all logic for CRUD operation in view.py file
   
Step 6:
    Declear all the end point in app.urls file after that we need to include in project urls.py

```python
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.product_list, name='product_list'),
]
```

app.urls
```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('fn_api/', include('fn_api.urls')),
]
```

### Flask

Requirement
```python
pip install Flask
pip install Flask-RESTful
pip install Flask-SQLAlchemy
```

Step 1:
    import required modules
```python
from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
```
Step2:
1. Initializing instance of flask app by declearing**  
```python
app = Flask(__name__)
```

Step3:
    Configure and Creating Database
```python
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///text.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
```
Step 4:
1. moving a step ahead by creating our model
```python
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    dob = db.Column(db.String(80), unique=True, nullable=False)
    def __init__(self,name, dob):
        self.name= name
        self.dob =dob

    def __repr__(self):
        return '<Name %r>' % self.name
```
Step 5:
    List all the records
```python
api = Api(app)
class UsersList(Resource):
    def get(self):
        return jsonify([{
            "id": user.id, 'name':user.name, "dob":user.dob
            } for user in User.query.all()
            #for user in User.query.all()
        ])
```
Single record
```python
class SingleUser(Resource):
    def get(self, num):
        user=User.query.filter_by(id=num).first_or_404()
        return jsonify([{
            "id": user.id, 'name':user.name, "dob":user.dob
        }])
```
Inserting New record
```python
class NewUser(Resource):
    def post(self):
        try:
            new_x = request.get_json()
            newuser=User(new_x['name'],new_x['dob'])
            db.session.add(newuser)
            db.session.commit()
            return {'message': 'POST data read successfully'}
        except:
            return {'message': 'Something went wrong'}
```
Deleting particular record from the table
```python
class deleteUser(Resource):
    def delete(self, num):
        try:
            todo = User.query.filter_by(id=num).first()
            db.session.delete(todo)
            db.session.commit()
            return {'message': 'User successfully deleted successfully'}
        except:
            return {'message': 'Something went wrong'}
```
Updating existing record 
```python
class UpdateUser(Resource):
    def put(self,id):
        print("hello")
        try:
            UpUser=User.query.filter_by(id=id).first()
            new_x = request.get_json()
            if new_x['name']:
                print(new_x['name'])
                UpUser.name=new_x['name']
            if new_x["dob"]:
                print("hello2")
                UpUser.dob =new_x['dob']
            db.session.commit()
            return {'message': 'Updated the data successfully'}
        except:
            return {'message': 'Something went wrong'}

    def patch(self,id):
        try:
            UpUser=User.query.filter_by(id=id).first()
            new_x = request.get_json()
            if new_x['name']:
                UpUser.name=new_x['name']
            if new_x["dob"]:
                UpUser.dob =new_x['dob']
            db.session.commit()
            return {'message': 'Updated the data successfully'}
        except:
            return {'message': 'Something went wrong'}
```
step 7:
    End points 
```python
api.add_resource(UsersList, '/')
api.add_resource(SingleUser, '/<int:num>')
api.add_resource(NewUser, '/user')
api.add_resource(deleteUser,"/delete/<int:num>")
api.add_resource(UpdateUser,"/user/<int:id>")
 ```
 
