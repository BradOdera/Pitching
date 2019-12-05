from flask import render_template,request,redirect,url_for
from . import main

# Views
@main.route('/')
def index():
	title = 'Pitches App'
	return render_template('index.html',title = title)


@main.route('/pitches')
def promotion_pitches():

    pitches = Pitch.get_pitches()

    return render_template("all_pitches.html", pitches = pitches)

@main.route('/pitch/<int:id>',methods = ['GET','POST'])
def pitch(id):
    pitch = Pitch.get_single_pitch(id)
    posted_date = pitch.posted.strftime('%b %d, %Y')

    return render_template('pitch.html', pitch=pitch, date=posted_date)