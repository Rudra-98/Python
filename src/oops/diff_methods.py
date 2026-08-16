class Student:
    school_name = "ABC High School"  # class variable
    total_students = 0                # class variable to track count

    def __init__(self, name, marks):
        self.name = name              # instance variable
        self.marks = marks            # instance variable
        Student.total_students += 1

    # Instance method — works with instance data (self)
    def show_details(self):
        print(f"Name: {self.name}, Marks: {self.marks}, School: {Student.school_name}")

    # Class method — works with class data (cls), not tied to one instance
    @classmethod
    def get_total_students(cls):
        return cls.total_students

    @classmethod
    def change_school_name(cls, new_name):
        cls.school_name = new_name

    # Static method — doesn't need self or cls, just a utility function grouped in the class
    @staticmethod
    def is_passing(marks):
        return marks >= 40


# ---- Usage ----

s1 = Student("Rudra", 85)
s2 = Student("Amit", 35)

# Instance method — called on an object
s1.show_details()   # Name: Rudra, Marks: 85, School: ABC High School
s2.show_details()   # Name: Amit, Marks: 35, School: ABC High School

# Class method — called on the class (or an instance, but conceptually class-level)
print(Student.get_total_students())   # 2

Student.change_school_name("XYZ International School")
s1.show_details()   # School name updated for ALL instances

# Static method — called on the class, no access to self/cls
print(Student.is_passing(85))   # True
print(Student.is_passing(35))   # False