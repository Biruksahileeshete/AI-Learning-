class Student:
    """Simple Student class"""
    def __init__(self, name, age, student_id):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.grades = []  # List to store grades
        self.courses = []  # List to store courses
    
    def add_grade(self, grade):
        """Add a grade (0-100)"""
        if 0 <= grade <= 100:
            self.grades.append(grade)
            return True
        return False
    
    def get_average(self):
        """Calculate average grade"""
        if len(self.grades) == 0:
            return 0
        total = 0
        for grade in self.grades:
            total = total + grade
        return total / len(self.grades)
    
    def enroll_course(self, course):
        """Enroll in a course"""
        self.courses.append(course)
    
    def show_info(self):
        """Display student information"""
        print("=" * 40)
        print(f"Student ID: {self.student_id}")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Average Grade: {self.get_average():.2f}")
        print(f"Courses: {', '.join(self.courses) if self.courses else 'None'}")
        print("=" * 40)

class Course:
    """Simple Course class"""
    def __init__(self, code, name, credits):
        self.code = code
        self.name = name
        self.credits = credits
        self.students = []  # List of student IDs
    
    def add_student(self, student_id):
        """Add a student to course"""
        self.students.append(student_id)
    
    def get_student_count(self):
        """Get number of students"""
        return len(self.students)
    
    def show_info(self):
        """Display course information"""
        print("=" * 40)
        print(f"Course Code: {self.code}")
        print(f"Course Name: {self.name}")
        print(f"Credits: {self.credits}")
        print(f"Students Enrolled: {self.get_student_count()}")
        print("=" * 40)
class School:
    """Main School Management System"""
    def __init__(self):
        self.students = []  # List to store all students
        self.courses = []   # List to store all courses
    
    def add_student(self, student):
        """Add a student to school"""
        self.students.append(student)
        print(f"✅ Student {student.name} added successfully!")
    
    def add_course(self, course):
        """Add a course to school"""
        self.courses.append(course)
        print(f"✅ Course {course.name} added successfully!")
    
    def find_student(self, student_id):
        """Find a student by ID"""
        for student in self.students:
            if student.student_id == student_id:
                return student
        return None
    
    def find_course(self, course_code):
        """Find a course by code"""
        for course in self.courses:
            if course.code == course_code:
                return course
        return None
    
    def enroll_student(self, student_id, course_code):
        """Enroll student in a course"""
        student = self.find_student(student_id)
        course = self.find_course(course_code)
        
        if student and course:
            student.enroll_course(course.name)
            course.add_student(student_id)
            print(f"✅ {student.name} enrolled in {course.name}")
            return True
        else:
            print("❌ Student or Course not found!")
            return False
    
    def show_all_students(self):
        """Display all students"""
        if len(self.students) == 0:
            print("📭 No students in the system")
            return
        
        print("\n" + "=" * 50)
        print("ALL STUDENTS")
        print("=" * 50)
        for student in self.students:
            print(f"ID: {student.student_id} | Name: {student.name} | Age: {student.age}")
        print("=" * 50)
    
    def show_all_courses(self):
        """Display all courses"""
        if len(self.courses) == 0:
            print("📭 No courses in the system")
            return
        
        print("\n" + "=" * 50)
        print("ALL COURSES")
        print("=" * 50)
        for course in self.courses:
            print(f"Code: {course.code} | Name: {course.name} | Credits: {course.credits}")
        print("=" * 50)
    
    def show_student_report(self, student_id):
        """Show detailed report for a student"""
        student = self.find_student(student_id)
        if student:
            student.show_info()
        else:
            print("❌ Student not found!")