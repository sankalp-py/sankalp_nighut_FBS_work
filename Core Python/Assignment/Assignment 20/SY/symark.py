class SYMarks:
    def __init__(self, computer_total, maths_total, electronics_total):
        self.computer_total = computer_total
        self.maths_total = maths_total
        self.electronics_total = electronics_total

    def __str__(self):
        return f"SY Marks - Computer: {self.computer_total}, Maths: {self.maths_total}, Electronics: {self.electronics_total}"
