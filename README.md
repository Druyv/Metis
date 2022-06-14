# Metis
Personal Innovation Project Nick Goris - HU Utrecht University of Applied Science, 2022

__THIS PROJECT IS CURRENTLY STILL IN DEVELOPMENT, SEE FINAL PARAGRAPH FOR A ROADMAP__

The Metis Project is, primarily, a framework/tool to automatically generate and commit feedback on submitted programming homework. The way the project is set up should allow an independance and agnosticity of the programming language and platform submitted to, but the base version will only support Python code submitted to Canvas (DLE used by HU).

This project was built to alleviate and/or remedy a few issues encountered at the HU Utrecht University of Applied Sciences during first year programming classes of the HBO-ICT major. Every year HBO-ICT attracts approximately 500 students who all take the same introductory programming classes - this volume is so large that the HU can't supply enough in-house lecturers, so external lecturers have to be hired. This has two main consequences: 1. Quality of feedback is inconsistent, and 2. Feedback cycle can be very long. Metis was thought up to help alleviate and, hopefully, eliminate these grievances.

One important note is that this project was never meant and should never be used to replace in person/face to face feedback sessions. It generates basic feedback (whether solutions function correctly) and performs basic code quality checks. In depth feedback should theoretically be possible, but is not the goal.

# Current Features
- Languages supported:
  - [Python](https://www.python.org/downloads/release/python-380/)
- Tools supported:
  - [PyLint](https://pylint.pycqa.org/en/latest/)
  - [UnitTest](https://docs.python.org/3/library/unittest.html)
- Platforms/DLE's supported:
  - [Canvas](https://www.instructure.com/)

- Automatically downloads all ungraded homework submissions (no personal data is ever stored)
- Automatically runs specified tests on all downloaded submissions
- Automatically runs specified tools on all downloaded submissions
- Automatically generated feedback from tests and tools
- Automatically posts feedback as comments on submissions

- Manually add new courses/assignments
- Manually update courses/assignments

# Future Features and Roadmap
- Language agnostic
- Tools can be user specified (will require additional programming for every tool)
- Platform agnostic (will require additional programming for every platform)

- Add new courses/assignments through web interface
- Update courses/assignments through web interface
- Run containerised
- Handle assignments that require user input
- Create insights based on (anonymous) data collected, e.g.:
  - What exercises students over- or underperform on
  - How long students take to complete an exercise on average
  - etc.

- Migrate all path operations to Python's PathLib
- Virtualise running of tests and tools, so asynchronous execution is easier
- Docker

# How to Install and Run
## Dependencies

This project has a few dependencies:
- [At least PythonV3.8](https://www.python.org/downloads/release/python-380/)
- [CanvasAPI library](https://canvasapi.readthedocs.io/en/stable/getting-started.html) - to be installed using `pip install canvasapi`
- [PyLint](https://pylint.pycqa.org/en/latest/) - to be installed using `pip install pylint`

# How to use
## Adding or updating a Course/Assignment

In the current version of the software, courses and assignments need to be added manually. They can be either in JSON or Python Dictionary format. 

# Credits

# License
