from SY.symark import SYMarks
from TY.tymark import TYMarks

class Student:
    def __init__(self, roll_no, name, sy_marks, ty_marks):
        self.roll_no = roll_no
        self.name = name
        self.sy_marks = sy_marks
        self.ty_marks = ty_marks

    def calculate_result(self):
    
        computer_total = self.sy_marks.computer_total + self.ty_marks.theory + self.ty_marks.practical

    
        if computer_total >= 70:
            grade = "A"
        elif computer_total >= 60:
            grade = "B"
        elif computer_total >= 50:
            grade = "C"
        elif computer_total >= 40:
            grade = "Pass Class"
        else:
            grade = "Fail"

        return computer_total, grade

    def display(self):
        total, grade = self.calculate_result()
        print("\n----- Student Result -----")
        print(f"Roll No   : {self.roll_no}")
        print(f"Name      : {self.name}")
        print(self.sy_marks)
        print(self.ty_marks)
        print(f"Computer Subject Total (SY + TY): {total}")
        print(f"Grade: {grade}")

if __name__ == "__main__":
    sy = SYMarks(computer_total=30, maths_total=45, electronics_total=40)
    ty = TYMarks(theory=25, practical=20)
    s1 = Student(roll_no=101, name="Mikey", sy_marks=sy, ty_marks=ty)
    s1.display()
