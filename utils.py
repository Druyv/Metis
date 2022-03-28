import os
from enum import Enum


def mkchdir(dir):
    """
    This functions tries to create a directory and change to that directory. If the directory already exists, it will
    simply move to the directory.

    :param dir: string representing the directory name
    """
    try:
        os.mkdir(dir.lower())
    except FileExistsError:
        pass
    finally:
        os.chdir(dir)


class FileType(Enum):
    PY = 1


class Tool(Enum):
    Pylint = 1