from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, IntegerField, FileField
from wtforms.validators import DataRequired

from canvasapi import Canvas

from credentials import API_URL, API_KEY, FLASK_KEY
from utils import FileType, Tool
from courses import courses

app = Flask(__name__)
app.config['SECRET_KEY'] = FLASK_KEY

canvas = Canvas(API_URL, API_KEY)

Bootstrap(app)

course = None

class ChooseCourseForm(FlaskForm):
    course      = IntegerField("Voer de Canvas cursus code in voor welk vak een opdracht toegevoegd moet worden: ")
    adding      = SubmitField(label="Opdracht(en) toevoegen")
    changing    = SubmitField(label="Opdracht(en) wijzigen")


class AddAssignmentForm(FlaskForm):
    assignment  = SelectField("Voor welke opdracht wil je tests toevoegen? ", choices = list(canvas.get_course(course).get_assignments()), coerce=int)
    filetype    = SelectField("Welk bestandstype wordt er ingeleverd? ", choices = [data.name for data in FileType])
    test_file   = FileField("Wat is het pad naar je testfile? ")
    tools       = SelectField("Welke tools wil je laten runnen? ", choices = [data.name for data in Tool])


class UpdateAssignmentForm(FlaskForm):
    if course in courses:
        assignment  = SelectField("Welke opdracht wil je updaten? ", choices = list(courses[course].values()), coerce=int)
        filetype    = SelectField("Welk bestandstype wordt er ingeleverd? ", choices=[data.name for data in FileType])
        test_file   = FileField("Wat is het pad naar je testfile? ")
        tools       = SelectField("Welke tools wil je laten runnen? ", choices=[data.name for data in Tool])


class PylintArgsForm(FlaskForm):
    # TODO: Radio field for basic options
    args = StringField("Geef eventuele overige opties op voor Pylint")


@app.route('/', methods=['GET', 'POST'])
def index():
    form = ChooseCourseForm()

    if form.validate_on_submit():
        if form.adding.data:
            pass

        elif form.changing.data:
            pass

    return render_template('index.html', form=form)
