# Student App

This program is a simple app that stores courses and students data and can assigns students to a course. It is a simple REST API written in python using Flask.

## REST API

A REST (REpresentational State Transfer) API (Application Programming Interface) is a transfer of resources (data) from a Server to a Client over the internet. Through the REST API, the client can perform a GET, POST, PUT, DELETE request on the server.

A client can use an API to request for resources from the server. A server has the resources and transfers it to the client through an API. A resource can be any object for example, user, photo, number. An API allows one software to talk to another. It is a procedure allowing a client to access the data from a server. 

An example of an API is `https://github.com/StephenDsouza90/demo-crud-sqlite-python-app` where:
 
github.com - Endpoint

/StephenDsouza90/demo-crud-sqlite-python-app - Resource in which 

/StephenDsouza90 is the parameter for the github username and /demo-crud-sqlite-python-app is the parameter for the github user's project name

## Flask

Flask is a mirco web framework written in Python. A microframework is a minimalistic web application framework which is constructed with a full-stack framework. It is designed to make getting started quick and easy and begins with a simple wrapper.

## The set up

This app runs with the Endpoint localhost (my computer) that has an IP address '0.0.0.0' (which maps to my computer) and a port 8080.
```
localhost:8080
```

In this app, the courses and students data has already been created in the `courses_data` and `students_data` objects respectively. The `assignment_data` object has an empty list through which the client can alter it as required.

### create_app()

The `create_app` function is responsible for defining the routes. These routes are mapped to the functions and these functions will be responsible for processing the client requests and send back responses.

The `create_app` function has the following functions and curl commands.

**courses data:**

1. Get all courses (GET request)
```
>> curl localhost:8080/courses
```
2. Add a new course (POST request)
```
>> curl -H "Content-Type: application/json" -X POST \
        -d "{\"course_id\":\"english\", \"name\":\"English\"}" \
        "localhost:8080/courses"
```
3. Get a particular course (GET request)
```
>> curl -X GET "localhost:8080/courses/math"
```
4. Delete a particular course (DELETE request)
```
>> curl -XDELETE "localhost:8080/courses/math"
```
5. Update a particular course (PUT request)
```
>> curl -H "Content-Type: application/json" -X PUT \
        -d "{\"course_id\":\"math\", \"name\":\"Advance Mathematics\"}" \
        "localhost:8080/courses/finance"
```

**students data:**

1. Get all students (GET request)
```
>> curl localhost:8080/students
```
2. Add a new student (POST request)
```
>> curl -H "Content-Type: application/json" -X POST \
        -d "{\"student_id\":4, \"name\":\"Ariana\"}" \
        "localhost:8080/students"
```
3. Get a particular student (GET request)
```
>> curl -X GET "localhost:8080/students/1"
```
4. Delete a particular student (DELETE request)
```
>> curl -XDELETE "localhost:8080/students/1"
```
5. Update a particular student (PUT request)
```
>> curl -H "Content-Type: application/json" -X PUT \
        -d "{\"student_id\":4, \"name\":\"Arie\"}" \
        "localhost:8080/students/4"
```

**assignments data:**

1. Assign a student to a course (POST request) 
```
>> curl -H "Content-Type: application/json" -X POST \
        -d "{\"student_id\":1, \"course_id\":\"math\"}" \
        "localhost:8080/assignments"
```
2. Get all assignments (GET request)
```
>> curl localhost:8080/assignments
```
3. Get courses of a particular student (GET request)
```
>> curl -X GET "localhost:8080/assignments/students/1"
```
4. Get total number of students in a particular course (GET request)
```
>> curl -X GET "localhost:8080/assignments/courses/math"
```
5. Delete a particular student from a course (DELETE request)
```
>> curl -XDELETE "localhost:8080/assignments/courses/math/1"
```

### route

The routing is showed below.

1. /courses for returning data about the courses saved in courses_data data structure
2. /students for returning data about the students saved in students_data data structure 
3. /assignments for returning data about the assignments saved in assignments_data data structure

Some of the routes have an additional parameter.

**Example:** 

The route for geting a particular course is '/courses/<course_id>'

### method type

The method types are

1. -X POST: Request for creating a resource 
2. -X GET: Request for reading a resource 
3. -X PUT: Request for updating a resource 
4. -XDELETE: Request for deleting a resource 

### curl command

An example of a curl command is as follows.

**Example:** 

Curl command for adding a new course to `courses_data`.

```
curl -H "Content-Type: application/json" 
     -X POST 
     -d "{\"course_id\":\"english\", \"name\":\"English\"}" 
     "localhost:8080/courses"
```

1. curl: stands for client
2. header: mentioning content type (only for POST or PUT)
3. method: instructions from client to server (POST, GET, PUT or DELETE)
3. data: the client provides the data in JSON format {key:value, key:value} (only for POST or PUT)
5. URL: "localhost:8080/courses" - URL is localhost:port/resource ((/parameter) (depending on the function))

### URL and route mapping

The URL maps to the route via the `app.route` decorator function which is part of the Flask Library. These functions are then responsible for processing client requests and returning responses.

**Route example:**
```
'/courses/<course_id>'
```

**URL example:**
```
"localhost:8080/courses/math"
```

## How to run locally:

Running the server
```
>> python rest.py

Serving on http://StephenDsouza:8080
Found course math
```

```
curl command
>> "localhost:8080/courses/math"

resource
{"course_id": "math", "name": "Mathematics"}
```