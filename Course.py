import os
from Exercise import Exercise


class Course:
    def __init__(self, course_name: str, course_code: int):
        self.course_name = course_name
        self.course_code = course_code
        self.exercises = []

    def __hash__(self):
        return hash(self.course_code)

    def __eq__(self, other):
        return self.course_code == other.course_code

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return repr(f"Course: {self.course_name}")

    def add_exercise(self, exercise: Exercise):
        self.exercises.append(exercise)

    def downloadSubmissions(self):
        if os.path.basename(os.getcwd()) != self.course_code:
            # Make directory for course and go there
            os.mkdir(str(self.course_code))
            os.chdir(str(self.course_code))

        for exercise in self.exercises:
            self.downloadSubmission(exercise)

    def downloadSubmission(self, exercise: Exercise):
        if os.path.basename(os.getcwd()) != exercise.exercise_code:
            # Make directory for exercise and go there
            os.mkdir(str(exercise.exercise_code))
            os.chdir(str(exercise.exercise_code))


