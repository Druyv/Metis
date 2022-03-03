# import os
from canvasapi import Canvas

api_url = 'https://canvas.hu.nl'
api_key = '11760~FKlrTGxmCScDMwFujVWxru2ylmIQ4QR8V68DzoQ6Zr4rTrk9xstO5pvcyOIAMdEV'
canvas = Canvas(api_url, api_key)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(canvas.get_current_user().get_profile())

    for course in canvas.get_courses():
        print(course)
