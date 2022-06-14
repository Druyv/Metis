Personal Innovation Project Nick Goris - HU Utrecht University of Applied Science, 2022

# Metis

__THIS PROJECT IS CURRENTLY STILL IN DEVELOPMENT, SEE [ROADMAP FOR FUTURE PLANS](https://github.com/Druyv/Metis/tree/development/README.md#features "Metis README Features")__

# Index
- [About](https://github.com/Druyv/Metis/tree/development#about "Metis README About")
- [Features](https://github.com/Druyv/Metis/tree/development#features "Metis README Features")
- [Setup](https://github.com/Druyv/Metis/tree/development/README.md#setup "Metis README Setup")
- [How to use](https://github.com/Druyv/Metis/tree/development/README.md#how-to-use "Metis README How to use")
- [Credits](https://github.com/Druyv/Metis/tree/development/README.md#credits "Metis README Credits")
- [License](https://github.com/Druyv/Metis/tree/development/README.md#license "Metis README License")

# About
The Metis Project is, primarily, a framework/tool to automatically generate and commit feedback on submitted programming homework. The way the project is set up should allow an independance and agnosticity of the programming language and platform submitted to, but the base version will only support Python code submitted to Canvas (DLE used by HU).

This project was built to alleviate and/or remedy a few issues encountered at the HU Utrecht University of Applied Sciences during first year programming classes of the HBO-ICT major. Every year HBO-ICT attracts approximately 500 students who all take the same introductory programming classes - this volume is so large that the HU can't supply enough in-house lecturers, so external lecturers have to be hired. This has two main consequences: 1. Quality of feedback is inconsistent, and 2. Feedback cycle can be very long. Metis was thought up to help alleviate and, hopefully, eliminate these grievances.

One important note is that this project was never meant and should never be used to replace in person/face to face feedback sessions. It generates basic feedback (whether solutions function correctly) and performs basic code quality checks. In depth feedback should theoretically be possible, but is not the goal.


# Features

<details>
  
<summary>Current feature list</summary>

- Languages supported:
  - [Python](https://www.python.org/downloads/release/python-380/ "Python 3.8 download page")
- Tools supported:
  - [PyLint](https://pylint.pycqa.org/en/latest/ "PyLint latest version page")
  - [UnitTest](https://docs.python.org/3/library/unittest.html "UnitTest documentation page")
- Platforms/DLE's supported:
  - [Canvas](https://www.instructure.com/ "Canvas Instructure homepage")

- Allows for automatically:
  - downloading all ungraded homework submissions for specified assignments (no personal data is ever stored)
  - running specified tests on all downloaded submissions
  - running specified tools on all downloaded submissions
  - generating feedback from test and tool results
  - posting feedback as comments on submissions
  - deleting downloaded submissions

- Allows for manually:
  - adding new courses/assignments
  - updating courses/assignments

</details>


<details>

<summary> Future features/roadmap </summary>
  
- Cleanup of project root folder
- Safer API key storage
- Automatic tests for development

- Language agnostic
- Tools can be user specified (will require additional programming for every tool)
- Platform agnostic (will require additional programming for every platform)

- Static CourseFactory
- Add new courses/assignments through web interface
- Update courses/assignments through web interface
- Run containerised for easier setup
- Handle assignments that require user input (currently unavailable because of a bug(?) in the subprocess module)
- Create insights based on (anonymous) data collected, e.g.:
  - What exercises students over- or underperform on
  - How long students take to complete an exercise on average
  - etc.


- Migrate all path operations to Python's PathLib
- Virtualise running of tests and tools, so asynchronous execution is easier

</details>


# Setup
## Installation
This project does not require any installation - clone the repo and you're ready to go! Do follow the [Dependencies](https://github.com/Druyv/Metis/tree/development#dependencies "Metis README Dependencies") and [How To Use Guide](https://github.com/Druyv/Metis/tree/development/README.md#how-to-use "Metis README How to use") links to find out how to set up the project properly.

## Dependencies
This project has a few dependencies:
- [At least PythonV3.8](https://www.python.org/downloads/release/python-380/ "Python 3.8 download page")
- [CanvasAPI library](https://canvasapi.readthedocs.io/en/stable/getting-started.html "Canvas API Getting Started page") - only if using Canvas; to be installed using `pip install canvasapi`
- [PyLint](https://pylint.pycqa.org/en/latest/ "PyLint latest version page") - only if using PyLint; to be installed using `pip install pylint`

## Actually setting it up

Setting up the project is rather easy - everything should work out of the box once all dependencies are installed and a few steps have been executed.

<details>
<summary> Setting up for use with Canvas </summary>

- __Canvas API key__:
  Canvas forbids one from requesting the users of their applications to provide their own API key, but I obviously cannot     give you mine. I would recommend asking your Canvas/DLE administrator to give you a key. Metis expects you to store this in a file called `credentials.py` in the root folder of the project (for now), with a variable name `API_KEY`
- __Canvas URL__:
  In the same `credentials.py` file you should add a variable `API_URL`, which comes down to your organisation's Canvas URL. For example, in the case of the HU, this is `https://canvas.hu.nl`

</details>

# How to use
## Adding or updating a Course/Assignment

In the current version of the software, courses and assignments need to be added manually. The skeleton for the dictionary is already set up in a file in the root folder called `courses.py`. 
Alternatively, a JSON file can be used following the same basic structure as the Python dictionary. Either the Python dictionary or the JSON file can then be fed into the appropriate `CourseFactory.makeNewCoursesFrom..(..)` function (as illustrated in `main.py`) to get the project to work.

<details>
<summary> Code example </summary>

```py
from CourseFactory import CourseFactory

course_factory = CourseFactory()
course_list_from_dict = course_factory.makeNewCoursesFromDict(<dict>)       #If a dict is used
course_list_from_json = course_factory.makeNewCoursesFromJson(<json_file>)  #If a JSON file is used
```
</details>

Once the webinterface for adding/changing courses/assignments, this step will no longer be necessary - but it is for now!

# Credits

# License
