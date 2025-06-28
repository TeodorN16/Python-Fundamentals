class Student:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.courses = []

    def view_courses(self):
        print(f"{self.name} is enrolled in: ")
        if len(self.courses) == 0:
            print("(No courses)")
        for course in self.courses:
            print(f"{course.name} ({course.ID})")

    def details(self):
        x = ",".join(course.name for course in self.courses)
        print(f"{self.name} with ID: {self.ID} is in courses [{x}]")

    def enroll(self, course):
        if course not in self.courses:
            self.courses.append(course)
            course.add_student(self)
            print(f"✅ Enrolled in {course.name}")
        else:
            print(f"Already enrolled in {course.name}.")

    def drop(self, name, ID):
        course_to_drop = None
        for course in self.courses:
            if course.name == name and course.ID == ID:
                course_to_drop = course
                break

        if course_to_drop:
            self.courses.remove(course_to_drop)
            course_to_drop.remove_student(self)
            print(f"✅ Dropped {course_to_drop.name}.")
        else:
            print("No course found.")

class Course:
    def __init__(self, name, ID):
        self.name = name
        self.ID = ID
        self.students = []

    def add_student(self, student):
        if student not in self.students:
            self.students.append(student)
            print(f"✅ Added {student.name} to {self.name}")
        else:
            print(f"{student.name} is already in {self.name}")

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)
            print(f"✅ Removed {student.name} from {self.name}")
        else:
            print(f"{student.name} is not enrolled in {self.name}")

    def view_students(self):
        if len(self.students) == 0:
            print("(No students)")
        else:
            for student in self.students:
                print(f"Student: {student.name} ({student.ID})")

teodor = Student("Teodor","S001")

physics = Course("Physics","C001")
math = Course("Math","C002")
teodor.enroll(physics)
teodor.enroll(math)

math.view_students()

teodor.view_courses()
teodor.details()
