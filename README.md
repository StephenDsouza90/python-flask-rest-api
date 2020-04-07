# Student App

This program is a simple app that stores courses and students data and can assigns students to a course. It is a simple REST API written in python using Flask and Flask-RESTPlus.

## REST API

A REST (REpresentational State Transfer) API (Application Programming Interface) is a transfer of resources (data) from a Server to a Client over the internet. Through the REST API, the client can perform a GET, POST, PUT, DELETE request on the server.

A client can use an API to request for resources from the server. A server has the resources and transfers it to the client through an API. A resource can be any object for example, user, photo, number. An API allows one software to talk to another. It is a procedure allowing a client to access the data from a server. 

An example of an API is `https://github.com/StephenDsouza90/demo-crud-sqlite-python-app` where:
 
github.com - Endpoint

/StephenDsouza90/demo-crud-sqlite-python-app - Resource in which 

/StephenDsouza90 is the parameter for the github username and /demo-crud-sqlite-python-app is the parameter for the github user's project name

## Flask

Flask is a mirco web framework written in Python. A microframework is a minimalistic web application framework which is constructed with a full-stack framework. It is designed to make getting started quick and easy and begins with a simple wrapper.

## Flask RESTPlus

Flask-RESTPlus is a Flask extension that supports building REST APIs quickly. It uses the best practices with minimal setup.

The classes in this app inherits the Resource class from Flask-RESTPlus through which HTTP methods are possible. The methods used in this app are GET, POST, PUT and DELETE. The routes are mapped to the respective classes and these classes have the methods which are responsible for processing the client requests and send back responses.

Flask-RESTPlus also handles the curl commands using Swagger's UI.

## Setup

This app runs in debug mode that has an IP address '127.0.0.1' and a port 5000.

```

http://127.0.0.1:5000/

```

In this app, the courses and students data has already been created in the `courses_data` and `students_data` objects respectively. The `assignment_data` object has an empty list through which the client can alter it as required.

## Routes

The routing is showed below.

1. /courses for returning data about the courses saved in courses_data data structure
2. /students for returning data about the students saved in students_data data structure 
3. /assignments for returning data about the assignments saved in assignments_data data structure

Some of the routes have an additional parameter.

**Example:** The route for geting a particular course is '/courses/<int:course_id>'

**Curl Command**

An example of a GET curl command is as follows.

Curl command for getting a particular course from `courses_data`.

```

>> curl -X GET "http://127.0.0.1:5000/courses/1" -H "accept: application/json"

```

**Response body**

```

{
  "course_name": "Mathematics",
  "course_id": 1
}

```

**Curl Command**

An example of a POST curl command is as follows. 

Curl command for adding a new course to `courses_data`.

```

curl -X POST "http://127.0.0.1:5000/courses" -H "accept: application/json" -H "Content-Type: application/json" -d "{ \"course_name\": \"English\"}"

```

**Response body**

```

{
  "message": "Success"
}

```

1. curl: stands for client
2. header: mentioning content type (only for POST or PUT)
3. method: instructions from client to server (POST, GET, PUT or DELETE)
3. data: the client provides the data in JSON format {key:value, key:value} (only for POST or PUT)
5. URL: "localhost:8080/courses" - URL is localhost:port/resource ((/parameter) (depending on the function))

## URL and Route Mapping

The URL maps to the route via the `api.route` decorator which is part of the Flask-RESTPlus Library. These functions are then responsible for processing client requests and returning responses.

## How to run locally:

Running the server

```

>> python rest.py

 * Serving Flask app "Student App" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: on
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 280-332-611
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)

```