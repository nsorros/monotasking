from flask import render_template

from app.forms import LoginForm
from app import app

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/prioritise")
def prioritise():
	tasks = [
		{
			'description': 'Design monotask logo'
		},
		{
			'description': 'Write blog spot'
		},
		{
			'description': 'Clean house'
		},
		{
			'description': 'Read book'
		}
	]
	return render_template('prioritise.html', tasks=tasks)

@app.route("/monotask")
def monotask():
	task = {
		'description': 'Design monotask logo'
	}
	return render_template('monotask.html', task=task)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template('login.html', 
                           title='Sign In',
                           form=form)
