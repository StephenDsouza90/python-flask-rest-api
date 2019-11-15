import flask
from flask import Flask, json
import waitress


# Standard server  responses
not_found = {"message": "Not Found"}
success = {"message": "Success"}
failed = {"message": "Failed"}

# Courses Data Resource: A list of courses data 
courses_data = [
    {"course_id": "math", "name": "Mathematics"},
    {"course_id": "python", "name": "Python Programming"},
    {"course_id": "finance", "name": "Finance"},
]

# Student Data Resource: A list of students data 
students_data = [
    {"student_id": 1, "name": "Stephen"},
    {"student_id": 2, "name": "Jude"},
    {"student_id": 3, "name": "Rachel"}
]

# Assignment Data Resource: A list of students assigned to courses 
assignment_data = [ ]


def create_app():
    """
    This function creates the server app and configures all the 
    GET, POST, PUT, DELETE routes for the resources.
    """
    app = Flask("Student App")


    @app.route('/courses', methods=['GET'])
    def get_courses():
        """
        GET request to get all courses:
            >> curl localhost:8080/courses
        """
        return json.dumps(courses_data)

    @app.route('/courses', methods=['POST'])
    def add_course():
        """
        POST request to add a new course:
            >> curl -H "Content-Type: application/json" -X POST -d "{\"course_id\":\"english\", \"name\":\"English\"}" "localhost:8080/courses"
        """
        course_id = flask.request.json["course_id"]
        course_name = flask.request.json["name"]
        new_course = {"course_id": course_id, "name": course_name}
        courses_data.append(new_course)
        print("Added new course {}".format(course_id))
        return json.dumps(success)

    @app.route('/courses/<course_id>', methods=['GET'])
    def get_course(course_id):
        """
        GET request to get a particular course:
            >> curl -X GET "localhost:8080/courses/math"
        """
        for c in courses_data:
            if c["course_id"] == course_id:
                print("Found course {}".format(course_id))
                return json.dumps(c)
        print("Course not found {}".format(course_id))
        return json.dumps(not_found), 404

    @app.route('/courses/<course_id>', methods=['DELETE'])
    def delete_course(course_id):
        """
        DELETE request to delete a particular course:
            >> curl -XDELETE "localhost:8080/courses/math"
        """
        for c in courses_data:
            if c["course_id"] == course_id:
                courses_data.remove(c)
                print("Deleted course {}".format(course_id))
                return json.dumps(success)
        print("Course not found {}".format(course_id))
        return json.dumps(not_found), 404

    @app.route('/courses/<course_id>', methods=['PUT'])
    def update_course(course_id):
        """
        UPDATE request to update a particular course:
            >> curl -H "Content-Type: application/json" -X PUT -d "{\"course_id\":\"math\", \"name\":\"Advance Mathematics\"}" "localhost:8080/courses/finance"
        """
        for c in courses_data:
            if c["course_id"] == course_id:
                new_course_name = flask.request.json["name"]
                c["name"] = new_course_name
                print("Updated course {}".format(course_id))
                return json.dumps(success)
        print("Course not updated {}".format(course_id))
        return json.dumps(not_found), 404

    @app.route('/students', methods=['GET'])
    def get_students():
        """
        GET request to get all students:
            >> curl localhost:8080/students
        """
        return json.dumps(students_data)

    @app.route('/students', methods=['POST'])
    def add_student():
        """
        POST request to add a new student:
            >> curl -H "Content-Type: application/json" -X POST -d "{\"student_id\":4, \"name\":\"Ariana\"}" "localhost:8080/students"
        """
        student_id = flask.request.json["student_id"]
        name = flask.request.json["name"]
        new_student_data = {"student_id":student_id, "name":name}
        students_data.append(new_student_data)
        print("Added new student {}".format(student_id))
        return json.dumps(success)

    @app.route('/students/<int:student_id>', methods=['GET'])
    def get_student(student_id):
        """
        GET request to get a particular student:
            >> curl -X GET "localhost:8080/students/1"
        """
        for s in students_data:
            if s["student_id"] == student_id:
                print("Found student {}".format(student_id))
                return json.dumps(s)
        print("Student not found {}".format(student_id))
        return json.dumps(not_found), 404

    @app.route('/students/<int:student_id>', methods=['DELETE'])
    def delete_student(student_id):
        """
        DELETE request to delete a particular student:
            >> curl -XDELETE "localhost:8080/students/1"
        """
        for s in students_data:
            if s["student_id"] == student_id:
                students_data.remove(s)
                print("Deleted student {}".format(student_id))
                return json.dumps(success)
        print("Student not found {}".format(student_id))
        return json.dumps(not_found), 404

    @app.route('/students/<int:student_id>', methods=['PUT'])
    def update_student(student_id):
        """
        UPDATE request to update a particular student:
            >> curl -H "Content-Type: application/json" -X PUT -d "{\"student_id\":4, \"name\":\"Arie\"}" "localhost:8080/students/4"
        """
        for s in students_data:
            if s["student_id"] == student_id:
                new_student_name = flask.request.json["name"]
                s["name"] = new_student_name
                print("Updated student {}".format(student_id))
                return json.dumps(success)
        print("Student not updated {}".format(student_id))
        return json.dumps(not_found), 404

    @app.route('/assignments', methods=['POST'])
    def assign_student_to_course():
        """
        POST request to assign student to a course:
            >> curl -H "Content-Type: application/json" -X POST -d "{\"student_id\":1, \"course_id\":\"math\"}" "localhost:8080/assignments"
        """
        student_id = flask.request.json["student_id"]
        course_id = flask.request.json["course_id"]
        assignment = {"student_id":student_id, "course_id":course_id}
        assignment_data.append(assignment)
        print("Assigned student {}".format(student_id))
        return json.dumps(success)

    @app.route('/assignments', methods=['GET'])
    def get_assignments():
        """
        GET request to get all assignments:
            >> curl localhost:8080/assignments
        """
        return json.dumps(assignment_data) 

    @app.route('/assignments/students/<int:student_id>', methods=['GET'])
    def get_courses_by_student(student_id):
        """
        GET request to get courses by a student:
            >> curl -X GET "localhost:8080/assignments/students/1"
        """
        found_course = False
        student_courses = []
        for i in assignment_data:
            if i["student_id"] == student_id:
                student_courses.append(i["course_id"])
                found_course = True
        if found_course:
            print(student_courses)
            return json.dumps(student_courses)
        else:
            print("Courses not found for {}".format(student_id))
            return json.dumps(not_found), 404

    @app.route('/assignments/courses/<course_id>', methods=['GET'])
    def total_students_in_course(course_id):
        """
        GET request to get total students in a particular course:
            >> curl -X GET "localhost:8080/assignments/courses/math"
        """
        found_course = False
        count_students = 0
        for i in assignment_data:
            if i["course_id"] == course_id:
                count_students += 1
                found_course = True
        if found_course:
            print(count_students)
            return json.dumps(count_students)
        else:
            print("Total not found for {}".format(course_id))
            return json.dumps(not_found), 404

    @app.route('/assignments/courses/<course_id>/<int:student_id>', methods=['DELETE'])
    def remove_student_from_course(course_id, student_id):
        """
        DELETE request to delete a particular student from a course:
            >> curl -XDELETE "localhost:8080/assignments/courses/math/1"
        """
        for i in assignment_data:
            if i["course_id"] == course_id and i["student_id"] == student_id:
                assignment_data.remove(i)
                print("Deleted student {}".format(student_id))
                return json.dumps(success)
        print("Student not found {}".format(student_id))
        return json.dumps(not_found), 404


    return app


# Start of program
def main():

    # Create the app with all the routes
    app = create_app()

    # Start the server
    # app.run(host='0.0.0.0', port='8080', server='gunicorn')
    waitress.serve(app, host='0.0.0.0', port=8080)


main()