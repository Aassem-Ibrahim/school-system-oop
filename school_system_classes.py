# school_system_classes
import random
from school_system_parameters import *


class UniqueIdGenerator:
    # This class is just generating random IDs for all elements used in the
    # system. Handling with ID is more efficient than using other methods.
    def __init__(self):
        self.generated_ids = []

    def generate_id(self):
        # generate random ID
        id = random.randint(1e8, 1e9)
        # make sure ID is unique
        while id in self.generated_ids:
            id = random.randint(1e8, 1e9)
        # add id generated to the list
        self.generated_ids.append(id)
        # return ID
        return id

    # remove generated id, when element in the system is removed
    def remove_id(self, id):
        try:
            # remove generated ID
            self.generated_ids.remove(id)
        except ValueError:
            # exception: not found in the list of generated ids
            print('DB Error: This ID is not generated')


# print 'Yes' or 'No' for console output
def yes_no(boolean):
    return 'Yes' if boolean else 'No'


class Professor:
    # This class holds professor's data (including: courses, salary, bonus)
    def __init__(self, id, name, age, address, phone):
        # personal info
        self.id = id            # random ID (or algorithmically generated ID)
        self.name = name        # personal name (first middle last)
        self.age = age          # age [integer]
        self.address = address  # address (apt., st., city, country)
        self.phone = phone      # phone number

        # info used by the system
        self.courses = []       # enrolled courses
        self.salary = "None"    # salary
        self.got_bonus = None   # bonus flag

    # when printing an object
    def __str__(self):
        return f"Name: {self.name} \n" + \
               f"Age: {self.age} \n" + \
               f"Address: {self.address} \n" + \
               f"Phone: {self.phone} \n" + \
               f"Salary: {self.salary} \n" + \
               f"Got Bonus: {yes_no(self.got_bonus)}"

    # when printing in on line
    def one_line_info(self):
        return f"{self.name}, {self.age}"

    # set salary for professor
    def set_salary(self, salary):
        self.salary = salary

    # check if professor will take a bonus at the end of the semester
    def update_bonus_status(self):
        # get number of courses of a professor
        number_of_courses = len(self.courses)
        # check threshold
        if number_of_courses >= PROFESSOR_COURSE_THRESHOLD_FOR_BONUS:
            # give bonus
            self.got_bonus = True
        else:
            # do not give bonus (less than threshold)
            self.got_bonus = False

    # add course to professor
    def add_course(self, course_id):
        # check if course is not added already
        if course_id not in self.courses:
            # add the course
            self.courses.append(course_id)
            # show sucessfully adding
            print(f'Course {course_id} added successfully to {self.id}')
        else:
            # show already exists
            print(f'Course {course_id} already exists in {self.id}')

    # remove course from professor
    def remove_course(self, course_id):
        try:
            # remove course from professor's courses
            self.courses.remove(course_id)
            # print success
            print(f'Course {course_id} is removed successfully from {self.id}')
        except ValueError:
            # exception: course not found in the courses list
            # print failure
            print(f'Course {course_id} is not in {self.id}')


class Student:
    # This class holds students's data (including: courses, region, full-time,
    #    academic probation, average grade)
    def __init__(self, id, name, age, address, phone):
        # personal info
        self.id = id            # random ID (or algorithmically generated ID)
        self.name = name        # personal name (first middle last)
        self.age = age          # age [integer]
        self.address = address  # address (apt., st., city, country)
        self.phone = phone      # phone number
        self.region = None      # region

        # info used by the system
        self.courses = []                       # enrolled courses
        self.is_full_time = 'Part-time'         # part/full time type
        self.is_on_academic_probation = None    # academic probation flag

    # when printing an object
    def __str__(self):
        return f"Name: {self.name} \n" + \
               f"Age: {self.age} \n" + \
               f"Address: {self.address} \n" + \
               f"Phone: {self.phone} \n" + \
               f"Number of Course: {len(self.courses)} \n" + \
               f"Region: {self.region} \n" + \
               f"Study: {self.is_full_time} \n" + \
               f"Academic Probation: {yes_no(self.is_on_academic_probation)}"

    # when printing in on line
    def one_line_info(self):
        # output to console in one line
        return f"{self.name}, {self.age}"

    # set local/international
    def set_region(self, is_local_flag):
        # check flag for local/international
        if is_local_flag:
            # set region to local
            self.region = 'Local'
        else:
            # set region to international
            self.region = 'International'

    # set part/full time (base on number of enrolled courses)
    def set_full_time(self, number_of_courses):
        if number_of_courses > MAX_PART_TIME_STUDENT_COURSES:
            self.is_full_time = 'Full-time'
        else:
            self.is_full_time = 'Part-time'

    # set academic probation (based on average grade)
    def set_academic_probation(self, average_grade):
        if average_grade < ACADEMIC_PROBATION_RATIO * COURSE_GRADE_RANGE:
            print(f"Student {self.name} is on academic probation")
            self.is_on_academic_probation = True
        else:
            print(f"Student {self.name} is 'not' on academic probation")
            self.is_on_academic_probation = False

    # add course to student
    def add_course(self, course_id):
        # make sure student does not exceed limit
        if len(self.courses) < MAX_NUMBER_OF_COURSES_PER_STUDENT:
            # check if course does not already exists
            if course_id not in self.courses:
                # add course
                self.courses.append(course_id)
                # change part/full time
                self.set_full_time(len(self.courses))
                # show successfully adding
                print(f'Course {course_id} added successfully to {self.id}')
            else:
                # show already exists
                print(f'Course {course_id} already exists in {self.id}')
        else:
            # show error message
            print('Error: Maximum number of courses reached (6)')

    # remove course from student
    def remove_course(self, course_id):
        try:
            # remove course
            self.courses.remove(course_id)
            # change part/full time
            self.set_full_time(len(self.courses))
            # show successfully adding
            print(f'Course {course_id} is removed successfully from {self.id}')
        except ValueError:
            # exception: course not found in the courses list
            print(f'Course {course_id} is not in {self.id}')


class Course:
    # This class holds courses's data (including: professors, students)
    def __init__(self, id, code, name, max_students_num, min_students_num):
        # basic course info
        self.id = id
        self.code = code
        self.name = name
        self.max_students_num = max_students_num
        self.min_students_num = min_students_num

        # info used by the system
        self.students_ids = []
        self.professors_ids = []
        self.status = 'enrollment state'

    # when printing an object
    def __str__(self):
        # info to be printed out
        students_count = len(self.students_ids)
        professors_count = len(self.professors_ids)
        students_range = f"{self.min_students_num}:{self.max_students_num}"
        # output to console
        return f"Course Name: {self.name} \n" + \
               f"Course ID: {self.code} \n" + \
               f"Students Range: [{students_range}] \n" + \
               f"Number of Enrolled Students: {students_count} \n" + \
               f"Number of Professors teaching: {professors_count} \n" + \
               f"Status: {self.status} \n"

    # when printing in on line
    def one_line_info(self, is_short_flag=True):
        # info to be printed
        students_range = f"{self.min_students_num}:{self.max_students_num}"
        current = len(self.students_ids)
        count_info = f", ({current}) of [{students_range}]" * is_short_flag
        # output to console in one line
        return f"{self.code}: {self.name}" + count_info

    # add professor to course
    def add_professor(self, professor_id):
        # check if professor is not added
        if professor_id not in self.professors_ids:
            # add professor
            self.professors_ids.append(professor_id)
            # return success
            return True
        else:
            # return failure
            return False

    # add student to course
    def add_student(self, student_id):
        # make sure students not exceeded the limit
        if len(self.students_ids) < self.max_students_num:
            # check if student is not added
            if student_id not in self.students_ids:
                # add student
                self.students_ids.append(student_id)
                # return success
                return True
            else:
                # return already exists
                return None
        else:
            # return failure
            return False

    # remove professor from course
    def remove_professor(self, professor_id):
        try:
            # remove professor from course
            self.professors_ids.remove(professor_id)
            # return success
            return True
        except ValueError:
            # exception: professor is not found in course
            # return failure
            return False

    # remove student from course
    def remove_student(self, student_id):
        try:
            # remove student from course
            self.students_ids.remove(student_id)
            # return success
            return True
        except ValueError:
            # exception: professor is not found in course
            # return failure
            return False
