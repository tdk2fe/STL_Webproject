from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
	user = {'nickname': 'Tim'}
	posts = [
		{
			'alderman': {'name': 'Megan Green'},
			'body': '15th ward'
		},
		{
			'alderman': {'name': 'Antonia French'},
			'body': '12th ward'
		}
	]
	return render_template('index.html',
		title='Home',
		user=user,
		posts=posts)