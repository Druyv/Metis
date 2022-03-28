import os

from Course import Course
from utils import mkchdir
from courses import courses

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        main_dir = os.getcwd()
        mkchdir("Courses")
        course_list = list()
        for course in courses:
            course_list.append(Course(course))

        for course in course_list:
            mkchdir(str(course.course_code))
            course.downloadSubmissions()
            course.runToolsAndTests()
            os.chdir("Courses")
