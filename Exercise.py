import os
from utils import mkchdir, FileType as FileType, Tool as Tool


class Exercise:
    """
    Exercise class
    """
    def __init__(self, exercise_code: int, file_type: FileType, testfile = None, tools = None,):
        """
        Constructor for Exercise object

        This class instantiates an Exercise obj. exercise_code is the exercise code of the exercise
        as found on Canvas, file_type is the type of file that the exercise is based on the FileType
        enum in utils, testfile is the file that contains the test for the exercise, and tools is a
        dict of strings containing the tool and the options for the tool.
        Testfile and tools can be added later.

        :param exercise_code:   int
        :param file_type:       FileType
        :param testfile:        str
        :param tools:           Key/Value pairs of Tool(enum type) and options for the tool(str)
        """
        self.exercise_code = exercise_code
        self.file_type = file_type
        self.testfile = testfile
        self.tools = tools if tools else {}
        print("HEllo Worlds")

    def __hash__(self):
        return hash(self.exercise_code)

    def __eq__(self, other):
        return self.exercise_code == other.exercise_code

    def __ne__(self, other):
        return not self == other

    def __repr__(self):
        return repr(f"Exercise: {self.exercise_code}")

    def addTool(self, tool):
        """
        Adds a tool to the exercise

        :param tool:    tool to add of Tools enum type
        """
        self.tools[tool] = []

    def addOptsToTool(self, tool, opts):
        """
        Adds options to a tool

        :param tool:    Tool enum type
        :param opts:    str
        """
        if not self.tools[tool]:
            self.tools[tool] = []
        self.tools[tool].append(opts)

    def downloadSubmissions(self, course_obj):
        """
        Downloads all submissions for the exercise, placing them in their own directory

        :param course_obj:  Canvas course object to get submissions from
        """
        # TODO: Check if submissions has been checked already
        # TODO: Actually download

        base_dir = os.getcwd()
        if os.path.basename(base_dir) != self.exercise_code:
            mkchdir(str(self.exercise_code))

        submission_list = course_obj.get_assignment(self.exercise_code).get_submissions()

        print(len(list(submission_list)))
        for submission in submission_list:
            try:
                if len(submission.attachments):
                    mkchdir(f'{submission.user_id}{submission.submitted_at}')
                    # Download submissions

            except:
                pass
            os.chdir(str(self.exercise_code))
        os.chdir(base_dir)

    def commentOnSubmission(self):
        """
        Reads feedback from file and posts it to the linked submission
        """
        return

    def runToolsAndTests(self):
        """
        Runs all tools and tests for the exercise
        """
        # TODO: Check if submissions has been checked already
        # TODO: Actually run tools and tests

        base_dir = os.getcwd()
        if os.path.basename(base_dir) != self.exercise_code:
            # Make directory for exercise and go there
            mkchdir(str(self.exercise_code))

        for submission in os.listdir():
            os.chdir(submission)
            # TODO: Run test file
            for tool, opts in self.tools.items():
                if tool == Tool.Pylint:
                    # pylint_opts = opts
                    # pylint.lint.Run(pylint_opts)
                    # TODO: Save feedback
                    pass
            # TODO: Post feedback: commentOnSubmission
            os.chdir(str(self.exercise_code))

        os.chdir(base_dir)
