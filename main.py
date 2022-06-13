#!usr/bin/env python
# -*- coding: utf-8 -*-

"""Automatic test- and feedback system for programming exercises"""

__author__      = "Nick Goris"

__version__     = "0.8"
__status__      = "Development"
__maintainer__  = "Nick Goris"
__email__       = "nick_goris@outlook.com"

import os
from datetime import datetime

from CourseFactory import CourseFactory
from utils import mkchdir, logDate
from courses import courses

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # print("Starting to check submissions to be graded")
    mkchdir("courses")

    course_factory = CourseFactory()
    course_list = course_factory.makeNewCoursesFromDict(courses)

    for course in course_list:
        # Downloading submissions for course in course_list
        course.downloadSubmissions()
        # Running tools and tests
        course.runToolsAndTests()
        os.chdir("..")

    #TODO: delete all downloaded submissions
    #os.rmdir("courses")


