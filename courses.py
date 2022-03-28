from utils import FileType as FileType
from utils import Tool as Tool

courses = {
    27193: {
        150429: {
            'filetype': FileType.Py,
            'tools': {Tool.Pylint: "Pylint opts"},
            'testfile': "define_some_testscript.py"
        },
        150430: {
            'filetype': FileType.PY,
            'tools': {Tool.Pylint: "Pylint opts"},
            'testfile': "define_some_testscript.py"
        }
    }
}
