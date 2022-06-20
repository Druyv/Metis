import os
import sys
from canvasapi import Canvas
from operator import add

from credentials import API_URL, API_KEY
from Exercise import Exercise
from utils import mkchdir


class Course:
    """
    Class to represent a course. Currently only supports Canvas cours
    """
    canvas = None
    try:
        canvas = Canvas(API_URL, API_KEY)
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
        return not self == other

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
        Downloads all submissions for all exercises in the course by calling the downloadSubmissions
        method from the Exercise objects.
        """
        mkchdir(str(self.course_code))
        for exercise in self.exercises:
            exercise.downloadSubmissions(self.course_obj)
        os.chdir("..")

    def runToolsAndTests(self):
        """
        Runs all tools and tests for all exercises in the course by calling the runToolsAndTests
        method from the Exercise objects.
        """
        os.chdir(str(self.course_code))
        for exercise in self.exercises:
            exercise.runToolsAndTests()
        os.chdir("..")
