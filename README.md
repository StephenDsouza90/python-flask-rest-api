# Application - Assigning students to courses

This program is a simple app that stores courses and students data and can assigns students to a course. It is a simple REST API written in python using Flask.

## REST API

A REST (REpresentational State Transfer) API (Application Programming Interface) is a transfer of resources (data) from a Server to a Client over the internet. Through the REST API, the client can perform a GET, POST, PUT, DELETE request on the server.

A client can use an API to request for resources from the server. A server has the resources and transfers it to the client through an API. A resource can be any object for example, user, photo, number. An API allows one software to talk to another. It is a procedure allowing a client to access the data from a server. 

An example of an API is "https://github.com/StephenDsouza90/demo-crud-sqlite-python-app" where:
 
github.com - Endpoint

/StephenDsouza90/demo-crud-sqlite-python-app - Resource in which 

/StephenDsouza90 is the parameter for the github username and /demo-crud-sqlite-python-app is the parameter for the github user's project name

## Flask

Flask is a mirco web framework written in Python. 

>>>>>> Need to write more on flask

## The set up

This app runs with the Endpoint localhost (my computer) that has an IP address '0.0.0.0' (which maps to my computer) and a port 8080.
```
localhost:8080
```

In this app, the courses and students data has already been created in the courses_data and students_data objects respectively. The assignment_data has an empty list through which the client can alter it as required.

### create_app()

The create_app function has the following functions and curl commands.

courses data:

1. Get all courses (GET request)
```
>> curl localhost:8080/courses
```
2. Add a new course (POST request)
```
>> curl -H "Content-Type: application/json" -X POST -d "{\"course_id\":\"english\", \"name\":\"English\"}" "localhost:8080/courses"
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
>> curl -H "Content-Type: application/json" -X PUT -d "{\"course_id\":\"math\", \"name\":\"Advance Mathematics\"}" "localhost:8080/courses/finance"
```

students data:

1. Get all students (GET request)
```
>> curl localhost:8080/students
```
2. Add a new student (POST request)
```
>> curl -H "Content-Type: application/json" -X POST -d "{\"student_id\":4, \"name\":\"Ariana\"}" "localhost:8080/students"
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
>> curl -H "Content-Type: application/json" -X PUT -d "{\"student_id\":4, \"name\":\"Arie\"}" "localhost:8080/students/4"
```

assignments data:

1. Assign a student to a course (POST request) 
```
>> curl -H "Content-Type: application/json" -X POST -d "{\"student_id\":1, \"course_id\":\"math\"}" "localhost:8080/assignments"
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

Example: URL for adding a new course to courses_data.

```
curl -H "Content-Type: application/json" -X POST -d "{\"course_id\":\"english\", \"name\":\"English\"}" "localhost:8080/courses"
```

1. URL: "localhost:8080/courses" - where the route is localhost/port/endpoint or host/port/endpoint/parameter (depending on the function) 
2. curl: stands for client
3. data: if it is a POST or PUT request, the client provides the data in JSON format {key:value, key:value}
4. header: mentioning content type (only for POST or PUT)