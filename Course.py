import os
from canvasapi import Canvas
from credentials import api_url, api_key
from utils import mkchdir
from Exercise import Exercise


class Course:
    canvas = None
    try:
        canvas = Canvas(api_url, api_key)
    except Exception as e:
        print(f'Exception occured: {e}')
        exit()

    def __init__(self, course_name: str, course_code: int):
        self.course_name = course_name
        self.course_code = course_code
        self.course_obj = self.canvas.get_course(course_code)
        self.exercises = list()

    def __hash__(self):
        return hash(self.course_code)

    def __eq__(self, other):
        return self.course_code == other.course_code

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return repr(f"Course: {self.course_name}")

    def addExercise(self, exercise: Exercise):
        self.exercises.append(exercise)

    def downloadSubmissions(self):
        base_dir = os.getcwd()
        if os.path.basename(base_dir) != self.course_code:
            # Make directory for course and go there
            mkchdir(str(self.course_code))

        for exercise in self.exercises:
            exercise.downloadSubmissions(self.course_obj)

        # Go back to original directory
        os.chdir(base_dir)

    def runToolsAndTests(self):
        for exercise in self.exercises:
            exercise.runToolsAndTests()

    def saveCourseObj(self):
        # saves course obj to file
        pass



