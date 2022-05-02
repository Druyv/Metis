import os

from CourseFactory import CourseFactory
from utils import mkchdir
from courses import courses

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print("Starting to check submissions to be graded")
    mkchdir("courses")

    course_factory = CourseFactory()
    course_list = course_factory.makeNewCoursesFromDict(courses)

    for course in course_list:
        print(f"Downloading submissions for {course.course_name}")
        course.downloadSubmissions()
        input("Everything has been downloaded, press enter to run tools")
        print(f"Running tools for {course.course_name}")
        course.runToolsAndTests()
        os.chdir("..")
    # TODO: Generate report/logging
    # print("Deleting submissions")
    # os.rmdir("courses")
    print("All done!")
