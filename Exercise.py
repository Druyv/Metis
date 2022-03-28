from utils import mkchdir, FileType as FileType, Tool as Tool
import os


class Exercise:
    def __init__(self, exercise_code: int, file_type: FileType, testfile = "", tools = None,):
        self.exercise_code = exercise_code
        self.file_type = file_type
        self.testfile = testfile
        self.tools = tools if tools else dict()

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

    def downloadSubmissions(self):
        if os.path.basename(os.getcwd()) != exercise.exercise_code:
            # Make directory for exercise and go there
            mkchdir(str(exercise.exercise_code))

        submission_list = self.course_obj.get_assignment(exercise.exercise_code).get_submissions()

        print(len(list(submission_list)))
        for submission in submission_list:
            try:
                if len(submission.attachments):
                    mkchdir(f'{submission.user_id}{submission.submitted_at}')
                    # Download submissions

            except:
                continue

    def runToolsAndTests(self):
        # chdir to exercise directory
        if os.path.basename(os.getcwd()) != self.exercise_code:
            # Make directory for exercise and go there
            mkchdir(str(self.exercise_code))

        for tool, opts in self.tools:
            if tool == Tool.Pylint:
                # pylint_opts = opts
                # pylint.lint.Run(pylint_opts)
                pass



