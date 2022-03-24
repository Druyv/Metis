import os
from canvasapi import Canvas
from credentials import api_url, api_key

from Course import Course
from Exercise import Exercise, FileType
from utils import mkchdir


try:
    canvas = Canvas(api_url, api_key)
except Exception as e:
    print(f'Exception occured: {e}')
    exit()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_dir = os.getcwd()
    print(main_dir)
    mkchdir("Courses")

    prog = Course('prog', 27193, canvas)
    prog.add_exercise(Exercise(150430,FileType.PY))
    prog.downloadSubmissions()