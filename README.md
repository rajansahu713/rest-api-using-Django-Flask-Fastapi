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


<img align="center" src="https://github.com/rajansahu713/CRUD-application-in-Flask/blob/main/images/django.png" width="500" height="350">
  
