class Course:
    def __init__(self, course_name: str, course_code: int):
        self.course_name = course_name
        self.course_code = course_code

    def __hash__(self):
        return hash(self.course_code)

    def __eq__(self, other):
        return self.course_code == other.course_code

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return repr(f"Course: {self.course_name}")
