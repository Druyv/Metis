import os
import sys
import requests
import pylint
from utils import mkchdir, chdirUpper, FileType as FileType, Tool as Tool
import credentials as cr
import json
import subprocess


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
        mkchdir(str(self.exercise_code))

        submission_list = course_obj.get_assignment(self.exercise_code).get_submissions()

        for submission in submission_list:
            try:
                if len(submission.attachments):
                    mkchdir(f'{submission.user_id}_{int(submission.submitted_at_date.timestamp())}')
                    for attachment in submission.attachments:
                        filepath = os.path.join(os.getcwd(), attachment['filename'])
                        if not os.path.exists(filepath):
                            with open(filepath, 'wb') as f:
                                f.write(requests.get(attachment['url'], allow_redirects=True, headers={'Authorization': f'Bearer {cr.API_KEY}'}).content)
                    os.chdir("..")
            except Exception as e:
                pass
        os.chdir("..")

    def commentOnSubmission(self):
        """
        Reads feedback from file and posts it to the linked submission
        """
        # TODO: Comment on submissions if feedback was generated
        return

    def runTools(self):
        """
        Runs the tools on the exercise files
        """
        for tool, opts in self.tools.items():
            if tool == Tool.Pylint:
                if "pylint.txt" in os.listdir():
                    continue
                if opts is not None:
                    args = ["pylint", opts, "--output=pylint.txt", os.listdir()[0]]
                else:
                    args = ["pylint", "--output=pylint.txt", os.listdir()[0]]
                subprocess.Popen(args).wait()

    def runTests(self):
        """
        Runs the tests on the exercise files
        """
        if self.testfile is not None:
            if "test_results.txt" not in os.listdir():
                if self.testfile not in os.listdir():
                    # TODO: Download testfile
                    pass
                args = ["python", self.testfile, "-v"]
                process = subprocess.check_output(args)
                with open("test_results.txt", "w") as f:
                    f.write(process.decode("utf-8"))

    def runToolsAndTests(self):
        """
        Runs all tools and tests for the exercise
        """
        os.chdir(str(self.exercise_code))
        for submission in os.listdir():
            os.chdir(submission)
            self.runTools()
            # self.runTests()
            # TODO: Post feedback: commentOnSubmission
            os.chdir("..")
        os.chdir("..")
