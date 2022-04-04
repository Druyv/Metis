import os
import sys
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
        sys.exit()

    def __init__(self, course_code):
        """
        Initializes a Course object.

        :param course_code: integer representing course code on Canvas
        """
        self.course_code = course_code
        self.course_obj = self.canvas.get_course(self.course_code)
        self.course_name = self.course_obj.name
        self.exercises = []

    def __hash__(self):
        return hash(self.course_code)

    def __eq__(self, other):
        return self.course_code == other.course_code

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return repr(f"Course: {self.course_name}")

    def addExercise(self, exercise: Exercise):
        """
        Adds an exercise to the exercise list.

        :param exercise:    Exercise object
        """
        self.exercises.append(exercise)

    def downloadSubmissions(self):
        """
        Downloads all submissions for all exercises in the course by calling the downloadSubmissions method from the
        Exercise objects.
        """
        base_dir = os.getcwd()
        if os.path.basename(base_dir) != self.course_code:
            # Make directory for course and go there
            mkchdir(str(self.course_code))

        for exercise in self.exercises:
            exercise.downloadSubmissions(self.course_obj)

        # Go back to original directory
        os.chdir(base_dir)

    def runToolsAndTests(self):
        """
        Runs all tools and tests for all exercises in the course by calling the runToolsAndTests method from the
        Exercise objects.
        """
        for exercise in self.exercises:
            exercise.runToolsAndTests()
