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
    except FileNotFoundError:
        print("Directory not found")
        exit()
    finally:
        os.chdir(new_dir)

def chdirUpper(new_dir):
    os.chdir("..")
    mkchdir(new_dir)


class FileType(Enum):
    """
    This class represents the different types of files that can be created.

    """
    Py = 1


class Tool(Enum):
    """
    This class represents the different tools that can be used to analyze the files.

    """
    Pylint = 1
