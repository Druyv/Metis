from Course import Course
'''
courses = {
    Course: {                       # Course object from Course.py
        assignment_id1: details,    # Canvas assignment id in int
        assignment_id2: details     # List of details
    },
    course_id2: {
        assignment_id1: details,
        assignment_id2: details
    }
}
'''

prog = Course('prog', 27193)

courses = {
    prog: {
        150429: []
    }
}