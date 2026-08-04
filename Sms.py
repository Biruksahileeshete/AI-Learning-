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