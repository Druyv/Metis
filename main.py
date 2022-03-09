# import os
from canvasapi import Canvas
from credentials import api_url, api_key
from courses import courses

try:
    canvas = Canvas(api_url, api_key)
except Exception as e:
    print(f'Exception occured: {e}')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    course_objects = []
    for course in courses:
        for assignment in courses[course]:
            print(canvas.get_course(course.course_code).get_assignment(assignment))