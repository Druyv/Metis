import os


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