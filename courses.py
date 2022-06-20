from utils import FileType as FileType, GradeType, default_passgrades
from utils import Tool as Tool

courses = {
    27193: {
        150441: {
            'filetype': FileType.Py,
            'gradetype': GradeType.PassFail,
            'passgrade': default_passgrades[GradeType.PassFail],
            'testfile': "test_27193_150441.py",
            'tools': {Tool.Pylint: "--disable=C0304, C0114"}
        },
        150445: {
            'filetype': FileType.Py,
            'gradetype': GradeType.PassFail,
            'passgrade': default_passgrades[GradeType.PassFail],
            'testfile': None,
            'tools': {Tool.Pylint: None}
        }
    }
}
