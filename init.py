from flask import Flask, render_template, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('init.html')

@app.route('/documentacao')
def documentation():
    return render_template('documentation.html')

@app.route('/videos')
def videos_page():
    return render_template('videos.html')

if __name__ == '__main__':
    app.run(debug=True)