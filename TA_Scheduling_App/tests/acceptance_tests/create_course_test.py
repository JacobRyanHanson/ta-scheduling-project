import datetime
from datetime import date, time

from django.test import TestCase, Client
from TA_Scheduling_App.models import User, Course


class AddCourseTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin = User(
            ROLE='ADMIN',
            FIRST_NAME='John',
            LAST_NAME='Doe',
            EMAIL='admin@example.com',
            PASSWORD_HASH='ad_password',
            PHONE_NUMBER='555-123-4567',
            ADDRESS='123 Main St',
            BIRTH_DATE=datetime.date(1990, 1, 1)
        )

        self.admin.save()

        self.instructor = User(
            ROLE='INSTRUCTOR',
            FIRST_NAME='Will',
            LAST_NAME='Doe',
            EMAIL='instructor@example.com',
            PASSWORD_HASH='ad_password',
            PHONE_NUMBER='555-123-4567',
            ADDRESS='123 Main St',
            BIRTH_DATE=date(1990, 1, 1)
        )

        self.instructor.save()

        # Log the user in
        self.credentials = {
            "email": "admin@example.com",
            "password": "ad_password"
        }
        self.client.post("/", self.credentials, follow=True)

    def test_create_course(self):
        self.course = Course(
            COURSE_NUMBER=151,
            INSTRUCTOR=self.instructor,
            COURSE_NAME='Introduction to Computer Science',
            COURSE_DESCRIPTION='An introductory course to the world of computer science.',
            SEMESTER='Fall 2023',
            PREREQUISITES='',
            DEPARTMENT='Computer Science'
        )

        self.course.save()

        self.course_data = {
            "courseNumber": 151,
            "instructorID": self.instructor.USER_ID,
            "courseName": 'Introduction to Computer Science',
            "courseDescription": 'An introductory course to the world of computer science.',
            "semester": 'Fall 2023',
            "prerequisites": '',
            "department": 'Computer Science'
        }

        response = self.client.post("/course-creation/", self.course_data)
        self.assertEqual(response.status_code, 200)

        self.assertEqual(len(Course.objects.filter(COURSE_NUMBER=self.course_data["courseNumber"])), 1)


class InvalidInputTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin = User(
            ROLE='ADMIN',
            FIRST_NAME='John',
            LAST_NAME='Doe',
            EMAIL='admin@example.com',
            PASSWORD_HASH='ad_password',
            PHONE_NUMBER='555-123-4567',
            ADDRESS='123 Main St',
            BIRTH_DATE=datetime.date(1990, 1, 1)
        )

        self.admin.save()

        self.instructor = User(
            ROLE='INSTRUCTOR',
            FIRST_NAME='Will',
            LAST_NAME='Doe',
            EMAIL='instructor@example.com',
            PASSWORD_HASH='ad_password',
            PHONE_NUMBER='555-123-4567',
            ADDRESS='123 Main St',
            BIRTH_DATE=date(1990, 1, 1)
        )

        self.instructor.save()

        # Log the user in
        self.credentials = {
            "email": "admin@example.com",
            "password": "ad_password"
        }
        self.client.post("/", self.credentials, follow=True)

    def test_invalid_blank(self):
        # Input fields are blank, but they are required (should not be possible)
        self.invalid_course_data = {
            "courseNumber": " ",  # Invalid
            "instructorID": " ",
            "courseName": '',
            "courseDescription": '',
            "semester": '',
            "prerequisites": '',
            "department": ''
        }
        with self.assertRaises(ValueError, msg="Invalid Inputs"):
            self.invalid_course = Course(
                COURSE_NUMBER=self.invalid_course_data["courseNumber"],
                INSTRUCTOR=self.instructor,
                COURSE_NAME=self.invalid_course_data["courseName"],
                COURSE_DESCRIPTION=self.invalid_course_data["courseDescription"],
                SEMESTER=self.invalid_course_data["semester"],
                PREREQUISITES=self.invalid_course_data["prerequisites"],
                DEPARTMENT=self.invalid_course_data["department"]
            )
            response = self.client.post("/course-creation/", self.invalid_course_data)

    def test_invalid_course_number(self):
        self.invalid_course_data = {
            "courseNumber": '$%^&*(',
            "instructorID": self.instructor.USER_ID,
            "courseName": 'Introduction to Computer Science',
            "courseDescription": 'An introductory course to the world of computer science.',
            "semester": 'Fall 2023',
            "prerequisites": '',
            "department": 'Computer Science'
        }
        with self.assertRaises(ValueError, msg="Invalid course number"):
            self.invalid_course = Course(
                COURSE_NUMBER=self.invalid_course_data["courseNumber"],
                INSTRUCTOR=self.instructor,
                COURSE_NAME=self.invalid_course_data["courseName"],
                COURSE_DESCRIPTION=self.invalid_course_data["courseDescription"],
                SEMESTER=self.invalid_course_data["semester"],
                PREREQUISITES=self.invalid_course_data["prerequisites"],
                DEPARTMENT=self.invalid_course_data["department"]
            )
        response = self.client.post("/course-creation/", self.invalid_course_data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_instructor(self):
        self.invalid_course_data = {
            "courseNumber": '191',
            "instructorID": '-7',
            "courseName": 'Introduction to Computer Science',
            "courseDescription": 'An introductory course to the world of computer science.',
            "semester": 'Fall 2023',
            "prerequisites": '',
            "department": 'Computer Science'
        }
        with self.assertRaises(ValueError):
            self.invalid_course = Course(
                COURSE_NUMBER=self.invalid_course_data["courseNumber"],
                INSTRUCTOR=self.invalid_course_data["instructorID"],
                COURSE_NAME=self.invalid_course_data["courseName"],
                COURSE_DESCRIPTION=self.invalid_course_data["courseDescription"],
                SEMESTER=self.invalid_course_data["semester"],
                PREREQUISITES=self.invalid_course_data["prerequisites"],
                DEPARTMENT=self.invalid_course_data["department"]
            )
        response = self.client.post("/course-creation/", self.invalid_course_data)
        self.assertEqual(response.context['status'], f'The instructor with id -7 does not exist.')

    def test_invalid_course_name(self):
        self.invalid_course_data = {
            "courseNumber": '191',
            "instructorID": self.instructor.USER_ID,
            "courseName": '_)(*&COMP',
            "courseDescription": 'An introductory course to the world of computer science.',
            "semester": 'Fall 2023',
            "prerequisites": '',
            "department": 'Computer Science'
        }
        with self.assertRaises(ValueError, msg="Invalid course name"):
            self.invalid_course = Course(
                COURSE_NUMBER=self.invalid_course_data["courseNumber"],
                INSTRUCTOR=self.instructor,
                COURSE_NAME=self.invalid_course_data["courseName"],
                COURSE_DESCRIPTION=self.invalid_course_data["courseDescription"],
                SEMESTER=self.invalid_course_data["semester"],
                PREREQUISITES=self.invalid_course_data["prerequisites"],
                DEPARTMENT=self.invalid_course_data["department"]
            )
        response = self.client.post("/course-creation/", self.invalid_course_data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_Description(self):
        self.invalid_course_data = {
            "courseNumber": '191',
            "instructorID": self.instructor.USER_ID,
            "courseName": 'Introduction to Computer Science',
            "courseDescription": '46880An introd%^uctory cou%&**rse to the world of computer science.',
            "semester": 'Fall 2023',
            "prerequisites": '',
            "department": 'Computer Science'
        }
        with self.assertRaises(ValueError, msg="Invalid course description"):
            self.invalid_course = Course(
                COURSE_NUMBER=self.invalid_course_data["courseNumber"],
                INSTRUCTOR=self.instructor,
                COURSE_NAME=self.invalid_course_data["courseName"],
                COURSE_DESCRIPTION=self.invalid_course_data["courseDescription"],
                SEMESTER=self.invalid_course_data["semester"],
                PREREQUISITES=self.invalid_course_data["prerequisites"],
                DEPARTMENT=self.invalid_course_data["department"]
            )
        response = self.client.post("/course-creation/", self.invalid_course_data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_semester(self):
        self.invalid_course_data = {
            "courseNumber": '191',
            "instructorID": self.instructor.USER_ID,
            "courseName": 'Introduction to Computer Science',
            "courseDescription": 'An introductory course to the world of computer science.',
            "semester": '!aaaaaaa!',
            "prerequisites": '',
            "department": 'Computer Science'
        }
        with self.assertRaises(ValueError, msg="Invalid course semester"):
            self.invalid_course = Course(
                COURSE_NUMBER=self.invalid_course_data["courseNumber"],
                INSTRUCTOR=self.instructor,
                COURSE_NAME=self.invalid_course_data["courseName"],
                COURSE_DESCRIPTION=self.invalid_course_data["courseDescription"],
                SEMESTER=self.invalid_course_data["semester"],
                PREREQUISITES=self.invalid_course_data["prerequisites"],
                DEPARTMENT=self.invalid_course_data["department"]
            )
        response = self.client.post("/course-creation/", self.invalid_course_data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_prerequisites(self):
        self.invalid_course_data = {
            "courseNumber": '191',
            "instructorID": self.instructor.USER_ID,
            "courseName": 'Introduction to Computer Science',
            "courseDescription": 'An introductory course to the world of computer science.',
            "semester": 'Fall 2023',
            "prerequisites": '4444',
            "department": 'Computer Science'
        }
        with self.assertRaises(ValueError, msg="Invalid course prerequisites"):
            self.invalid_course = Course(
                COURSE_NUMBER=self.invalid_course_data["courseNumber"],
                INSTRUCTOR=self.instructor,
                COURSE_NAME=self.invalid_course_data["courseName"],
                COURSE_DESCRIPTION=self.invalid_course_data["courseDescription"],
                SEMESTER=self.invalid_course_data["semester"],
                PREREQUISITES=self.invalid_course_data["prerequisites"],
                DEPARTMENT=self.invalid_course_data["department"]
            )
        response = self.client.post("/course-creation/", self.invalid_course_data)
        self.assertEqual(response.status_code, 200)

    def test_invalid_course_department(self):
        self.invalid_course_data = {
            "courseNumber": '191',
            "instructorID": self.instructor.USER_ID,
            "courseName": 'Introduction to Computer Science',
            "courseDescription": 'An introductory course to the world of computer science.',
            "semester": 'Fall 2023',
            "prerequisites": '',
            "department": 'C0mputer Science'
        }
        with self.assertRaises(ValueError, msg="Invalid course department"):
            self.invalid_course = Course(
                COURSE_NUMBER=self.invalid_course_data["courseNumber"],
                INSTRUCTOR=self.instructor,
                COURSE_NAME=self.invalid_course_data["courseName"],
                COURSE_DESCRIPTION=self.invalid_course_data["courseDescription"],
                SEMESTER=self.invalid_course_data["semester"],
                PREREQUISITES=self.invalid_course_data["prerequisites"],
                DEPARTMENT=self.invalid_course_data["department"]
            )
        response = self.client.post("/course-creation/", self.invalid_course_data)
        self.assertEqual(response.status_code, 200)


class DuplicateCreationFailTest(TestCase):
    def setUp(self):
        self.client = Client()

        self.admin = User(
            ROLE='ADMIN',
            FIRST_NAME='John',
            LAST_NAME='Doe',
            EMAIL='admin@example.com',
            PASSWORD_HASH='ad_password',
            PHONE_NUMBER='555-123-4567',
            ADDRESS='123 Main St',
            BIRTH_DATE=datetime.date(1990, 1, 1)
        )

        self.admin.save()

        self.instructor = User(
            ROLE='INSTRUCTOR',
            FIRST_NAME='Will',
            LAST_NAME='Doe',
            EMAIL='instructor@example.com',
            PASSWORD_HASH='ad_password',
            PHONE_NUMBER='555-123-4567',
            ADDRESS='123 Main St',
            BIRTH_DATE=date(1990, 1, 1)
        )

        self.instructor.save()

        self.course = Course(
            COURSE_NUMBER=151,
            INSTRUCTOR=self.instructor,
            COURSE_NAME='Introduction to Computer Science',
            COURSE_DESCRIPTION='An introductory course to the world of computer science.',
            SEMESTER='Fall 2023',
            PREREQUISITES='',
            DEPARTMENT='Computer Science'
        )

        self.course.save()

        self.course_data = {
            "courseNumber": 151,
            "instructorID": self.instructor.USER_ID,
            "courseName": 'Introduction to Computer Science',
            "courseDescription": 'An introductory course to the world of computer science.',
            "semester": 'Fall 2023',
            "prerequisites": '',
            "department": 'Computer Science'
        }

        # Log the user in
        self.credentials = {
            "email": "admin@example.com",
            "password": "ad_password"
        }
        self.client.post("/", self.credentials, follow=True)

    def test_duplicate_course(self):
        self.course_data2 = {
            "courseNumber": 151,
            "instructorID": self.instructor.USER_ID,
            "courseName": 'Introduction to Computer Science',
            "courseDescription": 'An introductory course to the world of computer science.',
            "semester": 'Fall 2023',
            "prerequisites": '',
            "department": 'Computer Science'
        }

        with self.assertRaises(ValueError):
            self.course2 = Course(
                COURSE_NUMBER=self.course_data2["courseNumber"],
                INSTRUCTOR=self.instructor,
                COURSE_NAME=self.course_data2["courseName"],
                COURSE_DESCRIPTION=self.course_data2["courseDescription"],
                SEMESTER=self.course_data2["semester"],
                PREREQUISITES=self.course_data2["prerequisites"],
                DEPARTMENT=self.course_data2["department"]
            )
            response = self.client.post("/course-creation/", self.course_data2)
            self.assertEqual(response, "Duplicate course number assignment failed", status_code=200)

        self.assertEqual(len(Course.objects.filter(COURSE_NUMBER=self.course_data2["courseNumber"])), 1)