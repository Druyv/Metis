from utils import FileType as FileType
from utils import Tool as Tool

courses = {
    27193: {
        150441: {
            'filetype': FileType.Py,
            'testfile': "test_27193_150441.py",
            'tools': {Tool.Pylint: "--disable=C0304, C0114"}
        },
        150445: {
            'filetype': FileType.Py,
            'testfile': None,
            'tools': {Tool.Pylint: None}
        }
    }
}
