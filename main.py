import os


from Course import Course
from Exercise import Exercise
from utils import mkchdir, FileType

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main_dir = os.getcwd()
    print(main_dir)
    mkchdir("Courses")

    prog = Course('prog', 27193)
    prog.addExercise(Exercise(150430,FileType.PY))
    prog.downloadSubmissions()
