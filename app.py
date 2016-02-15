from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('home.html')

@app.route("/add_task")
def add_task():
	return render_template('add_task.html')

if __name__ == "__main__":
    app.run(debug=True)