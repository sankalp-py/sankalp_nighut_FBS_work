class TYMarks:
    def __init__(self, theory, practical):
        self.theory = theory
        self.practical = practical

    def __str__(self):
        return f"TY Marks - Theory: {self.theory}, Practical: {self.practical}"
