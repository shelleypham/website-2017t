# do all the work here

from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('general/index.html', jobs = 0)

@app.route('/jobs')
def jobs():
    return render_template('general/jobs.html', jobs = 1)


#hello
if __name__ == "__main__":
    app.run()
