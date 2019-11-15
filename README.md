# Application - Assigning students to courses

This program is a simple app that stores courses and students data and can assigns students to a course. It is a simple REST API written in python using Flask.

## REST API

A REST (REpresentational State Transfer) API (Application Programming Interface) is a transfer of resources (data) from a Server to a Client over the internet.

A client uses an API to request for resources from the server. A server has the resources and transfers it to the client through an API. A resource can be any object for example, user, photo, number. 

An API allows one software to talk to another. It is a procedure allowing a client to access the data from a server. An example of an API is https://github.com/StephenDsouza90/demo-crud-sqlite-python-app where:
 
github.com/StephenDsouza90 - Endpoint URL

demo-crud-sqlite-python-app - Parameter

Through the REST API, the client can perform a GET, POST, PUT, DELETE request to the server.

## Flask

Flask is a mirco web framework written in Python. 

> Need to write more on flask

## Set up of rest.py 

This app runs on a localhost (my computer) with an IP address of '0.0.0.0' (which maps to my computer) and a port 8080 as an endpoint.

Example: 

github.com - Localhose

StephenDsouza90 - Endpoint

## How the app works

In this app, the courses and student data has already been created in the courses_data and students_data objects respectively. The assignment_data has an empty list through which the client can alter as required.

### create_app

The create_app function has the following methods for

courses data:

1. Get all courses (GET request)
2. Add a new course (POST request)
3. Get a particular course (GET request)
4. Delete a particular course (DELETE request)
5. Update a particular course (PUT request)

student data:

1. Get all students (GET request)
2. Add a new student (POST request)
3. Get a particular student (GET request)
4. Delete a particular student (DELETE request)
5. Update a particular student (PUT request)

assignment data:

1. Assign student to a course (POST request) 
2. Get all assignments (GET request)
3. Get a courses of a particular student (GET request)
4. Get total number of students in a particular course (GET request)
5. Delete a particular student from a course (DELETE request)

### routing, method type, url maping to function

The routing is done through 

localhost:8080/courses for courses_data

localhost:8080/students for students_data

localhost:8080/assignments for assignments_data

along with its respective parameter.

Example: The route for geting a particular course is '/courses/<course_id>'

The method types are for

GET: -X GET

POST: -X POST

PUT: -X PUT

DELETE: -XDELETE

The URL maps to function by providing the following details.

curl - Stands for client

route - host/port/endpoint or host/port/endpoint/parameter (depending on the function) 

data - if it is a POST or PUT request, the client provides the data in JSON format {key:value, key:value}

header - mentioning content type (only for POST or PUT)

Example: An example for adding a new course to courses_data.

curl -H "Content-Type: application/json" -X POST -d "{\"course_id\":\"english\", \"name\":\"English\"}" "localhost:8080/courses"