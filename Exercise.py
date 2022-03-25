from utils import FileType


class Exercise:
    def __init__(self, exercise_code: int, file_type: FileType, testfile = "", tools = None,):
        self.exercise_code = exercise_code
        self.file_type = file_type
        self.testfile = testfile
        self.tools = tools if tools else []

    def __hash__(self):
        return hash(self.exercise_code)

    def __eq__(self, other):
        return self.exercise_code == other.exercise_code

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return repr(f"Exercise: {self.exercise_code}")

    def addTool(self, tool):
        self.tools.append(tool)


