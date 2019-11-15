# Application - Assigning students to courses

This program is a simple app that stores courses and students data and can assigns students to a course. It is a simple REST API written in python using Flask.

## REST API

A REST (REpresentational State Transfer) API (Application Programming Interface) is a transfer of resources (data) from a Server to a Client over the internet. Through the REST API, the client can perform a GET, POST, PUT, DELETE request to the server.

A client uses an API to request for resources from the server. A server has the resources and transfers it to the client through an API. A resource can be any object for example, user, photo, number. An API allows one software to talk to another. It is a procedure allowing a client to access the data from a server. 

An example of an API is "https://github.com/StephenDsouza90/demo-crud-sqlite-python-app" where:
 
github.com/StephenDsouza90 - Endpoint URL

demo-crud-sqlite-python-app - Parameter

## Flask

Flask is a mirco web framework written in Python. 

>>>>>> Need to write more on flask

## Set up of rest.py 

This app runs on a localhost (my computer) with an IP address of '0.0.0.0' (which maps to my computer) and a port 8080 as an endpoint.

Example: 

github.com - Localhost

StephenDsouza90 - Endpoint

## How the app works

In this app, the courses and students data has already been created in the courses_data and students_data objects respectively. The assignment_data has an empty list through which the client can alter it as required.

### create_app()

The create_app function has the following methods for

courses data:

1. Get all courses (GET request)
2. Add a new course (POST request)
3. Get a particular course (GET request)
4. Delete a particular course (DELETE request)
5. Update a particular course (PUT request)

students data:

1. Get all students (GET request)
2. Add a new student (POST request)
3. Get a particular student (GET request)
4. Delete a particular student (DELETE request)
5. Update a particular student (PUT request)

assignments data:

1. Assign a student to a course (POST request) 
2. Get all assignments (GET request)
3. Get courses of a particular student (GET request)
4. Get total number of students in a particular course (GET request)
5. Delete a particular student from a course (DELETE request)

### routing

The routing is showed below

1. /courses for courses_data
2. /students for students_data
3. /assignments for assignments_data

Some of the routes have their respective parameter.

Example: The route for geting a particular course is '/courses/<course_id>'

### method type

The method types are

1. GET: -X GET
2. POST: -X POST
3. PUT: -X PUT
4. DELETE: -XDELETE

### url maping to function

The URL maps to function by follows.

Example: Adding a new course to courses_data.

curl -H "Content-Type: application/json" -X POST -d "{\"course_id\":\"english\", \"name\":\"English\"}" "localhost:8080/courses"

1. URL: "localhost:8080/courses" where the route is localhost/port/endpoint or host/port/endpoint/parameter (depending on the function) 
2. curl: stands for client
3. data: if it is a POST or PUT request, the client provides the data in JSON format {key:value, key:value}
4. header: mentioning content type (only for POST or PUT)