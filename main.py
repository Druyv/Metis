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
    base_dir = os.getcwd()
    print("Starting to check submissions to be graded")
    os.makedirs('logs', exist_ok=True)
    mkchdir("courses")

    course_factory = CourseFactory()
    course_list = course_factory.makeNewCoursesFromDict(courses)

    with open(f'{base_dir}\\logs\\{datetime.now().strftime("%d-%m-%Y-%H-%M")}_log.txt', 'a+') as f:
        try:
            total_download_count = 0
            f.write(f"{logDate()}: Running with version {__version__}\n")
            f.write(f"{logDate()}: Started running program\n")
            for course in course_list:
                f.write(f"{logDate()}: Downloading submissions for {course.course_name}\n")
                download_count = course.downloadSubmissions()
                total_download_count += download_count
                f.write(f"{logDate()}: Finished downloading {download_count} submissions\n")

                f.write(f"{logDate()}: Running tools and tests for {course.course_name}\n")
                course.runToolsAndTests()
                f.write(f"{logDate()}: Finished running tools and tests for {course.course_name}\n")

                os.chdir("..")
            f.write(f"{logDate()}: Finished running all tools and tests\n")

            f.write(f"{logDate()}: Deleting all downloaded submissions\n")
            # os.rmdir("courses")
            f.write(f"{logDate()}: All submissions deleted\n")
            f.write(f"{logDate()}: Finished running program\n")
        except Exception as e:
            f.write(e.__repr__())

        f.write(f"If any problems, inaccuracies or unexpected behaviour occurred, please contact {__maintainer__} at {__email__}")
