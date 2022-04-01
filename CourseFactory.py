from Course import Course
from Exercise import Exercise

class CourseFactory():
    def makeNewCoursesFromDict(self, dict):
        course_list = list()
        for course, assignments in dict.items():
            new_course = Course(course)
            for assignment, filetype, testfile, tools in assignments.items():
                new_course.addExercise(Exercise(assignment, filetype, testfile, tools))
            course_list.append(new_course)
        return course_list

    def saveCourse(self, course_objects, dest_file):
        with open(dest_file, 'a+') as file:
            for course in course_objects:
                file.write(course.export())
            pass
