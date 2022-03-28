from Course import Course
from utils import FileType as FileType
from utils import Tool as Tool
'''
courses = {
    Course: {                       # Course object from Course.py
        assignment_id1: details,    # Canvas assignment id in int
        assignment_id2: details     # List of details
    },
    course_id2: {
        assignment_id1: details,
        assignment_id2: details
    }
}
'''

prog = Course('prog', 27193)

courses = {
    prog: {
        150429: {
            'filetype': FileType.Py,
            'tools': {Tool.Pylint: "Pylint opts"},
            'testfile': "define_some_testscript.py"
        },
        150430: {
            'filetype': FileType.PY,
            'tools': {Tool.Pylint: "Pylint opts"},
            'testfile': "define_some_test}script.py"
        }
    }
}
