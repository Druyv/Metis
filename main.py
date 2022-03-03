# import os
from canvasapi import Canvas
from credentials import api_url, api_key

canvas = Canvas(api_url, api_key)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(canvas.get_current_user().get_profile())

    for course in canvas.get_courses():
        print(course)
