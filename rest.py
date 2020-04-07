from flask import Flask, request
from flask_restplus import Api, Resource, fields


app = Flask("Student App")
api = Api(app)


not_found = {"message": "Not Found"}
success = {"message": "Success"}
failed = {"message": "Failed"}


# Courses Data Resource: A list of courses data 
courses_data = [
    {"course_name": "Mathematics", "course_id": 1}
]

course = api.model("Course", {
    "course_name": fields.String("Course Name")
})


# Student Data Resource: A list of students data 
students_data = [
    {"student_name": "Stephen", "student_id": 1}
]

student = api.model("Student", {
    "student_name": fields.String("Student Name")
})


# Assignment Data Resource: A list of students assigned to courses 
assignment_data = [] # {"student_id": 1, "course_name": 1},

assignment = api.model("Assignment", {
    "student_id": fields.Integer(),
    "course_id": fields.Integer()
})


@api.route("/courses")
class Courses(Resource):

    def get(self):
        """ Get all courses """

        return courses_data

    @api.expect(course)
    def post(self):
        """ Add a new course """

        new_course = api.payload
        new_course["course_id"] = len(courses_data) + 1
        courses_data.append(new_course)
        return success, 201


@api.route("/courses/<int:course_id>")
class Course(Resource):

    def get(self, course_id):
        """ Get a particular course """ 

        for course in courses_data:
            if course["course_id"] == course_id:
                return course
        return not_found, 404
    
    def delete(self, course_id):
        """ Delete a particular course """

        for course in courses_data:
            if course["course_id"] == course_id:
                courses_data.remove(course)
                return success
        return not_found, 404

    @api.expect(course)
    def put(self, course_id):
        """ Update a particular course """

        for course in courses_data:
            if course["course_id"] == course_id:
                updated_course_name = api.payload["course_name"]
                course["course_name"] = updated_course_name
                return success
        return not_found, 404


@api.route("/students")
class Students(Resource):

    def get(self):
        """ Get all students """

        return students_data

    @api.expect(student)
    def post(self):
        """ Add a new student """

        new_student = api.payload
        new_student["student_id"] = len(students_data) + 1
        students_data.append(new_student)
        return success, 201


@api.route("/students/<int:student_id>")
class Student(Resource):

    def get(self, student_id):
        """ Get a particular student """

        for student in students_data:
            if student["student_id"] == student_id:
                return student
        return not_found, 404

    def delete(self, student_id):
        """ Delete a particular student """

        for student in students_data:
            if student["student_id"] == student_id:
                students_data.remove(student)
                return success
        return not_found, 404

    @api.expect(student)
    def put(self, student_id):
        """ Update a particular student """

        for student in students_data:
            if student["student_id"] == student_id:
                new_student_name = api.payload["student_name"]
                student["student_name"] = new_student_name
                return success
        return not_found, 404


@api.route("/assignments")
class Assignments(Resource):

    def get(self):
        """ Get all assignments """

        return assignment_data

    @api.expect(assignment)
    def post(self):
        """ Assign a student to a course """

        assignment_data.append(api.payload)
        return success, 201


@api.route("/assignments/students/<int:student_id>")
class CoursesByStudent(Resource):

    def get(self, student_id):
        """ Get courses by a student """

        found_course = False
        student_courses = []
        for i in assignment_data:
            if i["student_id"] == student_id:
                student_courses.append(i["course_id"])
                found_course = True
        if found_course:
            return student_courses
        else:
            return not_found, 404

@api.route("/assignments/courses/<int:course_id>")
class TotalStudentsInCourse(Resource):

    def get(self, course_id):
        """ Get total students in a course """

        found_course = False
        count_students = 0
        for i in assignment_data:
            if i["course_id"] == course_id:
                count_students += 1
                found_course = True
        if found_course:
            return count_students
        else:
            return not_found, 404

@api.route('/assignments/courses/<int:course_id>/<int:student_id>')
class RemoveStudentFromCourse(Resource):

    def delete(self, course_id, student_id):
        """ Remove student from course """

        for i in assignment_data:
            if i["course_id"] == course_id and i["student_id"] == student_id:
                assignment_data.remove(i)
                return success
        return not_found, 404


if __name__ == '__main__':
    app.run(debug=True)