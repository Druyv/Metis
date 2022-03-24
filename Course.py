import os
from canvasapi import Canvas

from utils import mkchdir
from Exercise import Exercise


class Course:
    def __init__(self, course_name: str, course_code: int, canvas_connection: Canvas):
        self.course_name = course_name
        self.course_code = course_code
        self.course_obj = canvas_connection.get_course(course_code)
        self.exercises = list()

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
            mkchdir(str(self.course_code))

        for exercise in self.exercises:
            self.downloadExerciseSubmissions(exercise)

    def downloadExerciseSubmissions(self, exercise: Exercise):
        if os.path.basename(os.getcwd()) != exercise.exercise_code:
            # Make directory for exercise and go there
            mkchdir(str(exercise.exercise_code))

        submission_list = self.course_obj.get_assignment(exercise.exercise_code).get_submissions()
        #
        # for submission in submission_list:
        #     if submission.attachments:
        #         mkchdir(str(submission.user_id))
        #         print(f"Downloading submission for {submission.user_id}")
        print(len(list(submission_list)))
        i = 0
        for submission in submission_list:
            try:
                if len(submission.attachments):
                    
            except:
                continue

        print(i)









