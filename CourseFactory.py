import json

from Course import Course
from Exercise import Exercise


class CourseFactory:
    """
    CourseFactory class
    """
    def makeNewCoursesFromDict(self, dict):
        """
        Creates a list of Course objects from a dictionary describing the courses

        :param dict: A dictionary describing the courses
        :return: list of Course objects
        """
        course_list = []
        for course, assignments in dict.items():
            new_course = Course(course)
            for assignment, details in assignments.items():
                new_course.addExercise(Exercise(assignment, details['filetype'], details['testfile'], details['tools']))
            course_list.append(new_course)
        return course_list

    def makeNewCoursesFromJson(self, json_file):
        """
        Creates a list of Course objects from a JSON file describing the courses by reading the JSON file
        and converting it to a dictionary, then passing this dict to makeNewCoursesFromDict

        :param json_file:
        :return: list of Course objects
        """
        return self.makeNewCoursesFromDict(json.loads(json_file))
