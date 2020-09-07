from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/", methods=['GET'])
@app.route("/jobs", methods=['GET'])
def jobs():
	return render_template('index.html')

