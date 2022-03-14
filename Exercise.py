from enum import Enum


class FileType(Enum):
    PY = 1


class Exercise:
    def __init__(self, exercise_code: int, file_type: FileType):
        self.exercise_code = exercise_code
        self.file_type = file_type

    def __hash__(self):
        return hash(self.exercise_code)

    def __eq__(self, other):
        return self.exercise_code == other.exercise_code

    def __ne__(self, other):
        return not(self == other)

    def __repr__(self):
        return repr(f"Exercise: {self.exercise_code}")
