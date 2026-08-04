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
# ========================================
# HELPER FUNCTIONS
# ========================================

def generate_student_id():
    """Generate a simple student ID"""
    import random
    return f"S{random.randint(100, 999)}"

def generate_course_code():
    """Generate a simple course code"""
    import random
    return f"C{random.randint(100, 999)}"

def get_valid_input(prompt, data_type=str):
    """Get valid input from user"""
    while True:
        try:
            user_input = input(prompt)
            if data_type == int:
                return int(user_input)
            elif data_type == float:
                return float(user_input)
            else:
                return user_input
        except ValueError:
            print("❌ Invalid input! Please try again.")

def print_menu():
    """Display main menu"""
    print("\n" + "=" * 50)
    print("📚 STUDENT MANAGEMENT SYSTEM")
    print("=" * 50)
    print("1. Add Student")
    print("2. Add Course")
    print("3. Enroll Student in Course")
    print("4. Add Grade")
    print("5. View All Students")
    print("6. View All Courses")
    print("7. View Student Report")
    print("8. Exit")
    print("=" * 50)
# ========================================
# MAIN PROGRAM
# ========================================

def main():
    """Main program loop"""
    school = School()  # Create school object
    running = True
    
    while running:
        print_menu()
        choice = input("Enter your choice (1-8): ")
        
        # 1. ADD STUDENT
        if choice == "1":
            print("\n--- ADD STUDENT ---")
            name = input("Student Name: ")
            age = get_valid_input("Age: ", int)
            student_id = generate_student_id()
            
            student = Student(name, age, student_id)
            school.add_student(student)
            print(f"📌 Student ID: {student_id}")
        
        # 2. ADD COURSE
        elif choice == "2":
            print("\n--- ADD COURSE ---")
            name = input("Course Name: ")
            code = generate_course_code()
            credits = get_valid_input("Credits: ", int)
            
            course = Course(code, name, credits)
            school.add_course(course)
            print(f"📌 Course Code: {code}")
        
        # 3. ENROLL STUDENT
        elif choice == "3":
            print("\n--- ENROLL STUDENT ---")
            student_id = input("Enter Student ID: ")
            course_code = input("Enter Course Code: ")
            school.enroll_student(student_id, course_code)
        
        # 4. ADD GRADE
        elif choice == "4":
            print("\n--- ADD GRADE ---")
            student_id = input("Enter Student ID: ")
            student = school.find_student(student_id)
            
            if student:
                grade = get_valid_input("Enter Grade (0-100): ", float)
                if student.add_grade(grade):
                    print(f"✅ Grade {grade} added to {student.name}")
                else:
                    print("❌ Invalid grade! Must be between 0-100")
            else:
                print("❌ Student not found!")
        
        # 5. VIEW ALL STUDENTS
        elif choice == "5":
            school.show_all_students()
        
        # 6. VIEW ALL COURSES
        elif choice == "6":
            school.show_all_courses()
        
        # 7. VIEW STUDENT REPORT
        elif choice == "7":
            print("\n--- STUDENT REPORT ---")
            student_id = input("Enter Student ID: ")
            school.show_student_report(student_id)
        
        # 8. EXIT
        elif choice == "8":
            print("\n👋 Goodbye! Keep learning!")
            running = False
        
        else:
            print("❌ Invalid choice! Please select 1-8")
        
        # Pause before showing menu again
        if running:
            input("\nPress Enter to continue...")
# ========================================
# RUN THE PROGRAM
# ========================================

if __name__ == "__main__":
    print("\n🎓 WELCOME TO STUDENT MANAGEMENT SYSTEM")
    print("Simple. Easy. Effective.\n")
    main()