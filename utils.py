import os
from enum import Enum


def mkchdir(new_dir):
    """
    This functions tries to create a directory and change to that directory. If the directory already exists, it will
    simply move to the directory.

    :param dir:     string representing the directory name
    """
    try:
        os.mkdir(new_dir.lower())
    except FileExistsError:
        pass
    finally:
        os.chdir(new_dir)


class FileType(Enum):
    """
    This class represents the different types of files that can be created.

    """
    PY = 1


class Tool(Enum):
    """
    This class represents the different tools that can be used to analyze the files.

    """
    Pylint = 1