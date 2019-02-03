from flask import Flask , render_template

app  Flask(__name__)

@app.route('/')
@app.route('/jobs')
ef jobs():
	return render_template('index.html')