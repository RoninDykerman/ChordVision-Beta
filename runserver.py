"""
This script runs the Test application using a development server.
"""

from datetime import datetime
from flask import render_template
from flask import Flask
app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template(
        'Test 7/Test/Test/templates/home.html',
        title='Home Page',
        year=datetime.now().year,
    )

@app.route('/library')
def library():
    return render_template(
        'Test 7/Test/Test/templates/library.html',
        year=datetime.now().year,
    )

@app.route('/hotel_california')
def hotel_california():
    return render_template(
        'Test 7/Test/Test/templates/hotel_california.html'
    )

@app.route('/hotel_california_legend')
def hotel_california_legend():
    return render_template(
        'Test 7/Test/Test/templates/hotel_california_legend.html'
    )

@app.route('/thatll_be_the_day')
def thatll_be_the_day():
    return render_template(
        'Test 7/Test/Test/templates/thatll_bethe_day.html'
    )

@app.route('/la_bamba')
def la_bamba():
    return render_template(
        'Test 7/Test/Test/templates/la_bamba.html'
    )

@app.route('/test')
def test():
    return render_template(
        'Test 7/Test/Test/templates/testSong.html'
    )

@app.route('/let_it_be')
def let_it_be():
    return render_template(
        'Test 7/Test/Test/templates/let_it_be.html'
    )

@app.route('/take_it_easy')
def take_it_easy():
    return render_template(
        'Test 7/Test/Test/templates/take_it_easy.html'
    )

@app.route('/come_on_lets_go')
def come_on_lets_go():
    return render_template(
        'Test 7/Test/Test/templates/come_on_lets_go.html'
    )

@app.route('/tutorial')
def tutorial():
    return render_template(
        'Test 7/Test/Test/templates/tutorial.html'
    )

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)