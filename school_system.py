'''
###############################################################################
#                           Statement of Requirement                          #
###############################################################################
>>> BLOCK #1:
A school needs a new system to track all of its students, professors and
courses. The school wants to keep track of what courses are offered, who
teaches each course and which students are enrolled in those courses. It
would also like to be able to track the grades of each of its students across
all courses. For each student and professor the school needs to know their
address, phone number, name and age.

>>> BLOCK #2:
Each course has a maximum and minimum number of students that they can enroll.
If the minimum number of students is not reached then the course will be
canceled. Each course is taught by at least one professor but sometimes may be
taught by many.

>>> BLOCK #3:
Professors are salaried employees at the school and therefore we need to keep
track of how much they make each year. If a professor teaches more than four
courses in a semester then they are granted a one time bonus of $20,000.

>>> BLOCK #4:
Students can be both local or international students and full or part time.
A student is considered a part time student if they are enrolled in 1 or 2
courses during any given semester. The maximum amount of courses a student
may be enrolled in at one time is 6. Students receive grades from each course,
these grades are numeric in the range of 0-100. Any students that have an
average grade across all enrolled courses lower than 60% is said to be on
academic probation.

NOTE: This system will be reset and updated at the end of each semester.
'''

from school_system_classes import UniqueIdGenerator, Professor, Student, Course


# clear console output
def clear_console():
    print("\033[H\033[J", end='\r')


# get index from user (make sure it is a number)
def get_index_from_user():
    index = input("\nSelect an index: ")
    while not index or not index.isnumeric():
        index = input("Select a valid index: ")
    return int(index)


# get personal info from user
def get_personal_info_from_user():
    name = input("Name: ")
    while not name:
        name = input("Name (valid): ")

    age = input("Age: ")
    while not age or not age.isnumeric():
        age = input("Age (valid): ")

    address = input("Address: ")
    while not address:
        address = input("Address (valid): ")

    phone = input("Phone: ")
    while not phone:
        phone = input("Phone (valid): ")

    return name, age, address, phone


# get region asking user
def get_region_flag_from_user():
    region = input("Region: Is local (y/n)? ")
    while not region or region.lower() not in ('yes', 'y', 'no', 'n'):
        region = input("Region (valid): Is local (y/n)? ")

    if region.lower() in ('yes', 'y'):
        return True
    else:
        return False


# get salary asking user
def get_salary_from_user():
    salary = input("Salary: ")
    while not salary or not salary.isnumeric():
        salary = input("Salary (valid): ")
    return salary


# get course basic info from user
def get_course_info_from_user():
    code = input("Code: ")
    while not code:
        code = input("Code (valid): ")

    name = input("Course Name: ")
    while not name:
        name = input("Course Name (valid): ")

    min_num = input("Min Number of Students: ")
    while not min_num or not min_num.isnumeric():
        min_num = input("Min Number of Students (valid): ")

    max_num = input("Max Number of Students: ")
    while not max_num or not max_num.isnumeric():
        max_num = input("Max Number of Students (valid): ")

    max_num, min_num = max(max_num, min_num), min(max_num, min_num)

    return code, name, max_num, min_num


# ask user for choice
def get_choice_from_user(boundries):
    choice = input("> Choose an option: ")
    while not choice or choice not in boundries:
        choice = input("> Choose a valid option: ")
    return choice


# semester naming in the system
semester_names = ("Fall", "Spring", "Summer")


class SchoolSystem:
    def __init__(self, name, year, semester):
        self.name = name
        self.year = year
        self.semester = semester
        self.id_generator = UniqueIdGenerator()

        self.courses = []
        self.students = []
        self.professors = []

        self.load_data()

    def __str__(self):
        year = f'{self.year}/{self.year + 1}'
        semester_name = semester_names[self.semester]
        return f"School Management System Information \n{'-'*35} \n" + \
               f"School Name: {self.name} \n" + \
               f"Year: {year} \n" + \
               f"Semester: {self.semester+1} ({semester_name}) \n\n" + \
               f"Statistics in recorded in the System \n{'-'*35} \n" + \
               f"No. of Courses: {len(self.courses)} \n" + \
               f"No. of Students: {len(self.students)} \n" + \
               f"No. of Professors: {len(self.professors)} \n"

    def load_data(self):
        # TODO: load data from file
        pass

    def save_data(self):
        # TODO: save data to file
        pass

    def show_menu(self):
        clear_console()

        print(self)
        print('Options')
        print('-------')
        print('1. Edit Students')
        print('2. Edit Professors')
        print('3. Edit Courses')
        print('4. Finish Semester (update then reset)')
        print('5. Save and Exit')
        print()

        choice = get_choice_from_user("12345")

        if choice == '1':
            self.edit_students()
        elif choice == '2':
            self.edit_professors()
        elif choice == '3':
            self.edit_courses()
        elif choice == '4':
            self.finish_semester()
        else:
            self.save_data()
            print('\nData was successfully saved.\nGoodbye')
            exit()

    def edit_students(self):
        clear_console()

        print('Edit Students')
        print('-------------')
        print('0. Back to Main Menu')
        print('1. Show Students List')
        print('2. Add Student')
        print('3. Remove Student')
        print('4. Edit/Show Student')
        print()

        choice = get_choice_from_user("01234")

        if choice == '1':
            self.show_students()
        elif choice == '2':
            self.add_student()
        elif choice == '3':
            self.remove_student()
        elif choice == '4':
            self.edit_a_student()
        elif choice == '0':
            self.show_menu()

    def list_students(self):
        if len(self.students) == 0:
            print("No students are added to the system yet")
        for i in range(len(self.students)):
            print("{:3d}. ".format(i+1) + self.students[i].one_line_info())

    def list_professors(self):
        if len(self.professors) == 0:
            print("No professors are added to the system yet")
        for i in range(len(self.professors)):
            print("{:3d}. ".format(i+1) + self.professors[i].one_line_info())

    def list_courses(self):
        if len(self.courses) == 0:
            print("No courses are added to the system yet")
        for i in range(len(self.courses)):
            print("{:3d}. ".format(i+1) + self.courses[i].one_line_info())

    def show_students(self):
        clear_console()

        print("All Students in the System")
        print("--------------------------")
        self.list_students()

        input("\nPress <enter> to go back ")

        self.edit_students()

    def add_student(self):
        clear_console()

        print("New Student Form")
        print("----------------")
        id = self.id_generator.generate_id()
        name, age, address, phone = get_personal_info_from_user()
        region_flag = get_region_flag_from_user()

        self.students.append(Student(id, name, age, address, phone))
        self.students[-1].set_region(region_flag)

        print("\nStudent is added successfully")

        input("\nPress <enter> to go back ")
        self.edit_students()

    def remove_student(self):
        clear_console()

        print("Remove Student Request")
        print("----------------------")
        students_count = len(self.students)
        if students_count:
            self.list_students()

            index = get_index_from_user()

            if index < 1 or index > students_count:
                self.remove_students()
                return
            else:
                student_index = index - 1
                student_id = self.students[student_index].id

                del self.students[student_index]
                self.remove_student_id_from_all_courses(student_id)

                print("\nStudent is removed successfully")
        else:
            print("No students are in the system to be removed")

        input("\nPress <enter> to go back ")
        self.edit_students()

    def remove_student_id_from_all_courses(self, student_id):
        for i in self.courses:
            i.remove_student(student_id)

    def edit_a_student(self):
        clear_console()

        print("Edit Student Information")
        print("------------------------")
        students_count = len(self.students)
        if students_count:
            self.list_students()
            index = get_index_from_user()

            if index < 1 or index > students_count:
                self.edit_a_student()
                return
            else:
                self.edit_a_specific_student(index - 1)
        else:
            print("No students are in the system to be edited")

        input("\nPress <enter> to go back ")
        self.edit_students()

    def edit_a_specific_student(self, index):
        clear_console()

        print("Edit Student Information")
        print("------------------------")
        print(self.students[index])
        print()
        print("Enrolled Courses")
        print("----------------")
        self.show_courses_of_specific_student(index)

        print()
        print("Options")
        print("-------")
        print("0. Back to Students Edit")
        print("1. Edit info")
        print("2. Add Course")
        print("3. Remove Course")

        print()

        choice = get_choice_from_user("0123")

        if choice == '1':
            self.edit_a_specific_student_info(index)
        elif choice == '2':
            self.add_course_to_specific_student(index)
        elif choice == '3':
            self.remove_course_from_specific_student(index)
        elif choice == '0':
            self.edit_students()

    def get_course_name(self, id):
        for course in self.courses:
            if course.id == id:
                return course.name
        else:
            return "Error in DB"

    def show_course_by_id(self, id, is_short_flag):
        for course in self.courses:
            if course.id == id:
                return course.one_line_info(is_short_flag)
        else:
            return "Error in DB"

    def show_professor_by_id(self, id):
        for professor in self.professors:
            if professor.id == id:
                return professor.one_line_info()
        else:
            return "Error in DB"

    def show_student_by_id(self, id):
        for student in self.students:
            if student.id == id:
                return student.one_line_info()
        else:
            return "Error in DB"

    def show_courses_of_specific_student(self, index):
        courses_count = len(self.students[index].courses)
        if courses_count:
            courses = self.students[index].courses
            for i in range(courses_count):
                print(f"{i+1}. " + self.show_course_by_id(courses[i], False))
        else:
            print("Student is not enrolled in any courses")

    def edit_a_specific_student_info(self, index):
        clear_console()

        print("Edit Student Information for")
        print("----------------------------")
        print(self.students[index])
        print()

        name, age, address, phone = get_personal_info_from_user()
        region_flag = get_region_flag_from_user()

        self.students[index].name = name
        self.students[index].age = age
        self.students[index].address = address
        self.students[index].phone = phone
        self.students[index].set_region(region_flag)

        print("\nStudent info is updated successfully")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_student(index)

    def add_course_to_specific_student(self, index):
        clear_console()

        student_name = self.students[index].name
        print(f"Add Course to Student: {student_name}")
        print(f"-----------------------{'-'*len(student_name)}")
        courses_count = len(self.courses)
        if courses_count:
            self.list_courses()
            course_index = get_index_from_user()

            if course_index < 1 or course_index > courses_count:
                self.add_course_to_specific_student(index)
                return
            else:
                print()
                course_index = course_index - 1
                course_id = self.courses[course_index].id
                student_id = self.students[index].id

                status = self.courses[course_index].add_student(student_id)
                if status is True:
                    self.students[index].add_course(course_id)
                elif status is None:
                    print("Course already exists")
                else:
                    print("Error: Maximum number of students reached")

        else:
            print("No courses are in the system to be edited")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_student(index)

    def remove_course_from_specific_student(self, index):
        clear_console()

        student_name = self.students[index].name
        print(f"Remove Course from Student: {student_name}")
        print(f"----------------------------{'-'*len(student_name)}")

        courses_count = len(self.students[index].courses)
        if courses_count:
            self.show_courses_of_specific_student(index)
            course_index = get_index_from_user()

            if course_index < 1 or course_index > courses_count:
                self.remove_course_from_specific_student(index)
                return
            else:
                print()
                course_index = course_index - 1
                course_id = self.students[index].courses[course_index]
                student_id = self.students[index].id

                self.students[index].remove_course(course_id)
                self.courses[course_index].remove_student(student_id)
        else:
            print("This student is not enrolled in any course yet")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_student(index)

    def edit_professors(self):
        clear_console()

        print('Edit Professors')
        print('---------------')
        print('0. Back to Main Menu')
        print('1. Show Professors List')
        print('2. Add Professor')
        print('3. Remove Professor')
        print('4. Edit/Show Professor')
        print()

        choice = get_choice_from_user("01234")

        if choice == '1':
            self.show_professors()
        elif choice == '2':
            self.add_professor()
        elif choice == '3':
            self.remove_professor()
        elif choice == '4':
            self.edit_a_professor()
        elif choice == '0':
            self.show_menu()

    def show_professors(self):
        clear_console()

        print("All Professors in the System")
        print("--------------------------")
        self.list_professors()

        input("\nPress <enter> to go back ")

        self.edit_professors()

    def add_professor(self):
        clear_console()

        print("New Professor Form")
        print("------------------")
        id = self.id_generator.generate_id()
        name, age, address, phone = get_personal_info_from_user()
        salary = get_salary_from_user()

        self.professors.append(Professor(id, name, age, address, phone))
        self.professors[-1].set_salary(salary)

        print("\nProfessor is added successfully")

        input("\nPress <enter> to go back ")
        self.edit_professors()

    def remove_professor(self):
        clear_console()

        print("Remove Professor Request")
        print("------------------------")
        professors_count = len(self.professors)
        if professors_count:
            self.list_professors()
            index = get_index_from_user()

            if index < 1 or index > professors_count:
                self.remove_professor()
                return
            else:
                professor_index = index - 1
                professor_id = self.students[professor_index].id

                del self.professors[professor_index]
                self.remove_professor_id_from_all_courses(professor_id)

                print("\nProfessor is removed successfully")
        else:
            print("No Professors are in the system to be removed")

        input("\nPress <enter> to go back ")
        self.edit_professors()

    def remove_professor_id_from_all_courses(self, professor_id):
        for i in self.courses:
            i.remove_professor(professor_id)

    def edit_a_professor(self):
        clear_console()

        print("Edit Professor Information")
        print("--------------------------")
        professors_count = len(self.professors)
        if professors_count:
            self.list_professors()
            index = get_index_from_user()

            if index < 1 or index > professors_count:
                self.edit_a_professor()
                return
            else:
                self.edit_a_specific_professor(index - 1)
        else:
            print("No Professors are in the system to be edited")

        input("\nPress <enter> to go back ")
        self.edit_professors()

    def edit_a_specific_professor(self, index):
        clear_console()

        print("Edit Professor Information")
        print("--------------------------")
        print(self.professors[index])
        print()
        print("Enrolled Courses")
        print("----------------")
        self.show_courses_of_specific_professor(index)

        print()
        print("Options")
        print("-------")
        print("0. Back to Professors Edit")
        print("1. Edit info")
        print("2. Add Course")
        print("3. Remove Course")
        print()

        choice = input("> Choose an option: ")
        while choice not in '0123':
            choice = input("> Choose a valid option: ")

        if choice == '1':
            self.edit_a_specific_professor_info(index)
        elif choice == '2':
            self.add_course_to_specific_professor(index)
        elif choice == '3':
            self.remove_course_from_specific_professor(index)
        elif choice == '0':
            self.edit_professors()

    def show_courses_of_specific_professor(self, index):
        courses_count = len(self.professors[index].courses)
        if courses_count:
            courses = self.professors[index].courses
            for i in range(courses_count):
                print(f"{i+1}. " + self.show_course_by_id(courses[i], False))
        else:
            print("Professor is not teaching any courses")

    def edit_a_specific_professor_info(self, index):
        clear_console()

        print("Edit Professor Information for")
        print("------------------------------")
        print(self.professors[index])
        print()

        name, age, address, phone = get_personal_info_from_user()
        salary = get_salary_from_user()

        self.professors[index].name = name
        self.professors[index].age = age
        self.professors[index].address = address
        self.professors[index].phone = phone
        self.professors[index].set_salary(salary)

        print("\nProfessor info is updated successfully")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_professor(index)

    def add_course_to_specific_professor(self, index):
        clear_console()

        professor_name = self.professors[index].name
        print(f"Add Course to Professor: {professor_name}")
        print(f"-------------------------{'-'*len(professor_name)}")
        courses_count = len(self.courses)
        if courses_count:
            self.list_courses()
            course_index = get_index_from_user()

            if course_index < 1 or course_index > courses_count:
                self.add_course_to_specific_professor(index)
                return
            else:
                print()
                course_index = course_index - 1
                course_id = self.courses[course_index].id
                professor_id = self.professors[index].id

                self.professors[index].add_course(course_id)
                self.courses[course_index].add_professor(professor_id)
        else:
            print("No courses are in the system to be edited")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_professor(index)

    def remove_course_from_specific_professor(self, index):
        clear_console()

        professor_name = self.professors[index].name
        print(f"Remove Course from Professor: {professor_name}")
        print(f"------------------------------{'-'*len(professor_name)}")

        courses_count = len(self.professors[index].courses)
        if courses_count:
            self.show_courses_of_specific_professor(index)
            course_index = get_index_from_user()

            if course_index < 1 or course_index > courses_count:
                self.remove_course_from_specific_professor(index)
                return
            else:
                print()
                course_index = course_index - 1
                course_id = self.professors[index].courses[course_index]
                professor_id = self.professors[index].id

                self.professors[index].remove_course(course_id)
                self.courses[course_index].remove_professor(professor_id)
        else:
            print("This professor is not teaching any courses yet")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_professor(index)

    def edit_courses(self):
        clear_console()

        print('Edit Courses')
        print('------------')
        print('0. Back to Main Menu')
        print('1. Show Courses List')
        print('2. Add Course')
        print('3. Remove Course')
        print('4. Edit/Show Course')
        print()

        choice = get_choice_from_user("01234")

        if choice == '1':
            self.show_courses()
        elif choice == '2':
            self.add_course()
        elif choice == '3':
            self.remove_course()
        elif choice == '4':
            self.edit_a_course()
        elif choice == '0':
            self.show_menu()

    def show_courses(self):
        clear_console()

        print("All Courses in the System")
        print("--------------------------")
        self.list_courses()

        input("\nPress <enter> to go back ")

        self.edit_courses()

    def add_course(self):
        clear_console()

        print("New Course Form")
        print("---------------")
        id = self.id_generator.generate_id()
        code, name, max_num, min_num = get_course_info_from_user()

        self.courses.append(Course(id, code, name, max_num, min_num))

        print("\nCourse is added successfully")

        input("\nPress <enter> to go back ")
        self.edit_courses()

    def remove_course(self):
        clear_console()

        print("Remove Course Request")
        print("---------------------")
        courses_count = len(self.courses)
        if courses_count:
            self.list_courses()

            index = get_index_from_user()

            if index < 1 or index > courses_count:
                self.remove_course()
                return
            else:
                course_index = index - 1
                course_id = self.courses[course_index].id

                print()
                del self.courses[course_index]
                self.remove_course_id_from_all(course_id)

                print("\nCourse is removed successfully")
        else:
            print("No Courses are in the system to be removed")

        input("\nPress <enter> to go back ")

        self.edit_courses()

    def remove_course_id_from_all(self, course_id):
        # remove from all professors
        for professor in self.professors:
            professor.remove_course(course_id)
        # remove from all students
        for student in self.students:
            student.remove_course(course_id)

    def edit_a_course(self):
        clear_console()

        print("Edit Course Information")
        print("-----------------------")
        courses_count = len(self.courses)
        if courses_count:
            self.list_courses()
            index = get_index_from_user()

            if index < 1 or index > courses_count:
                self.edit_a_course()
                return
            else:
                course_index = index - 1
                self.edit_a_specific_course(course_index)
        else:
            print("No Courses are in the system to be edited")

        input("\nPress <enter> to go back ")
        self.edit_courses()

    def edit_a_specific_course(self, index):
        clear_console()

        print("Edit Course Information")
        print("------------------------")
        print(self.courses[index])

        print("Professors Teaching")
        print("-------------------")
        self.show_professors_of_specific_course(index)
        print()
        print("Enrolled Students")
        print("-----------------")
        self.show_students_of_specific_course(index)

        print()
        print("Options")
        print("-------")
        print("0. Back to Courses Edit")
        print("1. Edit info")
        print("2. Add Professor")
        print("3. Add Student")
        print("4. Remove Professor")
        print("5. Remove Student")
        print()

        choice = get_choice_from_user("012345")

        if choice == '1':
            self.edit_a_specific_course_info(index)
        elif choice == '2':
            self.add_professor_to_specific_course(index)
        elif choice == '3':
            self.add_student_to_specific_course(index)
        elif choice == '4':
            self.remove_professor_from_specific_course(index)
        elif choice == '5':
            self.remove_student_from_specific_course(index)
        elif choice == '0':
            self.edit_courses()

    def show_professors_of_specific_course(self, index):
        professors = self.courses[index].professors_ids
        professors_count = len(professors)
        if professors_count:
            for i in range(professors_count):
                print(f"{i+1}. " + self.show_professor_by_id(professors[i]))
        else:
            print("No Professor is teaching this course yet")

    def show_students_of_specific_course(self, index):
        students = self.courses[index].students_ids
        students_count = len(students)
        if students_count:
            for i in range(students_count):
                print(f"{i+1}. " + self.show_student_by_id(students[i]))
        else:
            print("No Student is enrolled in this course yet")

    def edit_a_specific_course_info(self, index):
        clear_console()

        print("Edit Course Information for")
        print("----------------------------")
        print(self.courses[index])
        print()

        code, name, max_num, min_num = get_course_info_from_user()

        self.courses[index].code = code
        self.courses[index].name = name
        self.courses[index].max_students_num = max_num
        self.courses[index].min_students_num = min_num

        print("\nCourse info is updated successfully")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_course(index)

    def add_professor_to_specific_course(self, index):
        clear_console()

        course_name = self.courses[index].name
        print(f"Add Professor to Course: {course_name}")
        print(f"-------------------------{'-'*len(course_name)}")
        professors_count = len(self.professors)
        if professors_count:
            self.list_professors()
            professor_index = get_index_from_user()

            if professor_index < 1 or professor_index > professors_count:
                self.add_professor_to_specific_course(index)
                return
            else:
                print()
                professor_index = professor_index - 1
                course_id = self.courses[index].id
                professor_id = self.professors[professor_index].id

                self.professors[professor_index].add_course(course_id)
                self.courses[index].add_professor(professor_id)
        else:
            print("No courses are in the system to be edited")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_course(index)

    def add_student_to_specific_course(self, index):
        clear_console()

        course_name = self.courses[index].name
        print(f"Add Student to Course: {course_name}")
        print(f"-----------------------{'-'*len(course_name)}")
        students_count = len(self.students)
        if students_count:
            self.list_students()
            student_index = get_index_from_user()

            if student_index < 1 or student_index > students_count:
                self.add_student_to_specific_course(index)
                return
            else:
                print()
                student_index = student_index - 1
                course_id = self.courses[index].id
                student_id = self.students[student_index].id

                status = self.courses[index].add_student(student_id)
                if status is True:
                    self.students[student_index].add_course(course_id)
                elif status is None:
                    print("Course already exists")
                else:
                    print("Error: Maximum number of students reached")

        else:
            print("No courses are in the system to be edited")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_course(index)

    def remove_professor_from_specific_course(self, index):
        clear_console()

        course_name = self.courses[index].name
        print(f"Remove Professor from Course: {course_name}")
        print(f"------------------------------{'-'*len(course_name)}")

        professors_count = len(self.courses[index].professors_ids)
        if professors_count:
            self.show_students_of_specific_course(index)
            prof_index = get_index_from_user()

            if prof_index < 1 or prof_index > professors_count:
                self.remove_professor_from_specific_course(index)
                return
            else:
                print()
                prof_index = prof_index - 1
                professors_id = self.courses[index].professors_ids[prof_index]
                course_id = self.courses[index].id

                self.professors[prof_index].remove_course(course_id)
                self.courses[index].remove_professor(professors_id)
        else:
            print("This course has no teaching professors yet")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_course(index)

    def remove_student_from_specific_course(self, index):
        clear_console()

        course_name = self.courses[index].name
        print(f"Remove Student from Course: {course_name}")
        print(f"----------------------------{'-'*len(course_name)}")

        students_count = len(self.courses[index].students_ids)
        if students_count:
            self.show_students_of_specific_course(index)
            student_index = get_index_from_user()

            if student_index < 1 or student_index > students_count:
                self.remove_student_from_specific_course(index)
                return
            else:
                print()
                student_index = student_index - 1
                student_id = self.courses[index].students_ids[student_index]
                course_id = self.courses[index].id

                self.students[student_index].remove_course(course_id)
                self.courses[index].remove_student(student_id)
        else:
            print("This course has no enrolled students yet")

        input("\nPress <enter> to go back ")
        self.edit_a_specific_course(index)

    def finish_semester(self):
        clear_console()

        # update and reset each professor
        for professor in self.professors:
            # update bonus for professor
            professor.update_bonus_status()
            # remove all courses from professor
            professor.courses = []

        print("Collecting grades from all students courses")
        print("-------------------------------------------")
        # update and reset each student
        for student in self.students:
            # print info
            print()
            print(f"For student {student.name}:")
            print(f"-------------{'-'*len(student.name)}")
            # calculate average grade for student
            avg_grade = self.calculate_avg_grade(student.courses)
            # check if student has courses
            if len(student.courses):
                # determine academic probation
                student.set_academic_probation(avg_grade)
            else:
                # show that student has no courses
                print("This student has not enrolled in any course")
            # remove all courses from student
            student.courses = []
            # reset part/full time until the student enroll in more than two
            #   courses again
            student.is_full_time = 'Part-time'

        # update and reset courses
        for course in self.courses:
            # remove all professors from course
            course.professors_ids = []
            # remove all students from course
            course.students_ids = []
            # change status to 'enrollment again'
            course.status = 'enrollment state'

        # update year and semester
        self.semester = (self.semester + 1) % 3
        self.year = self.year + 1 if not self.semester else self.year

        print("\nSuccessfully Finishing Semester")

        input("\nPress <enter> to go back ")
        self.show_menu()

    def calculate_avg_grade(self, courses):
        # get number of student courses
        student_courses_count = len(courses)
        # check if number is positive
        if not student_courses_count:
            # no need to calculate any or loop over an empty courses list
            return
        else:
            # average grade equals 0 at first
            avg_grade = 0
            # loop over
            for i in range(student_courses_count):
                # course name in input
                course_name = f"{i+1}. {self.get_course_name(courses[i])}"
                # ask user to enter grade
                grade = input(course_name + ": ")
                # make sure grade is inputed correctly
                while not grade or not grade.isnumeric():
                    grade = input(course_name + " (valid): ")
                # sum grades
                avg_grade += int(grade)
            # calculate average grade
            avg_grade /= student_courses_count
            # show average grade
            print("\nAverage grade is %.2f" % (avg_grade))
            print("Semester GPA is %.2f\n" % (avg_grade/25))
            # return average grade
            return avg_grade


if __name__ == "__main__":
    system = SchoolSystem('ACU', 2020, 0)
    system.students.append(Student(id=system.id_generator.generate_id(),
                                   name="Aassem Ibrahim Sehsah",
                                   age=23,
                                   address="Algaish St., KSH",
                                   phone="0111-111-1111"))
    system.students.append(Student(id=system.id_generator.generate_id(),
                                   name="Alaa Ibrahim Sehsah",
                                   age=21,
                                   address="Algaish St., KSH",
                                   phone="0123-456-7890"))
    system.professors.append(Professor(id=system.id_generator.generate_id(),
                                       name="Amira Ibrahim Sehsah",
                                       age=25,
                                       address="Algaish St., KSH",
                                       phone="0101-234-5678"))
    system.professors[0].set_salary(5750)
    system.courses.append(Course(id=system.id_generator.generate_id(),
                                 code="SW312",
                                 name="Software Engineering II",
                                 max_students_num=1,
                                 min_students_num=0))
    system.courses.append(Course(id=system.id_generator.generate_id(),
                                 code="SW345",
                                 name="Specialized Software",
                                 max_students_num=90,
                                 min_students_num=10))
    system.courses.append(Course(id=system.id_generator.generate_id(),
                                 code="CS222",
                                 name="Computer Modeling",
                                 max_students_num=100,
                                 min_students_num=20))
    system.courses.append(Course(id=system.id_generator.generate_id(),
                                 code="CS231",
                                 name="Database II",
                                 max_students_num=80,
                                 min_students_num=5))
    system.courses.append(Course(id=system.id_generator.generate_id(),
                                 code="CS221",
                                 name="Database I",
                                 max_students_num=160,
                                 min_students_num=40))
    system.courses.append(Course(id=system.id_generator.generate_id(),
                                 code="SW387",
                                 name="Requirements Engineering",
                                 max_students_num=120,
                                 min_students_num=20))
    system.courses.append(Course(id=system.id_generator.generate_id(),
                                 code="SW398",
                                 name="Graduation Project I",
                                 max_students_num=1000,
                                 min_students_num=0))
    system.courses.append(Course(id=system.id_generator.generate_id(),
                                 code="SW399",
                                 name="Graduation Project II",
                                 max_students_num=1000,
                                 min_students_num=0))

    system.students[0].courses = [system.courses[0].id,
                                  system.courses[1].id,
                                  system.courses[2].id,
                                  system.courses[3].id,
                                  system.courses[4].id,
                                  system.courses[5].id]
    system.students[1].courses = [system.courses[0].id,
                                  system.courses[1].id]
    system.show_menu()

    pass
