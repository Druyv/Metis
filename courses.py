from utils import FileType as FileType
from utils import Tool as Tool

courses = {
    27193: {
        150441: {
            'filetype': FileType.Py,
            'testfile': "define_some_testscript.py",
            'tools': {Tool.Pylint: "Pylint opts"}
        },
        150445: {
            'filetype': FileType.Py,
            'testfile': "define_some_testscript.py",
            'tools': {Tool.Pylint: "Pylint opts"}
        }
    }
}
