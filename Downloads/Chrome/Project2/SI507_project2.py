# Import statements necessary
from flask import Flask, render_template
from movies_tools import*
import csv
import random
import codecs
import sys
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)


app = Flask(__name__)


@app.route('/')
def hello_world():
    with open("movies_clean.csv","r", encoding = 'utf8') as f:
        reader = csv.reader(f)
        count_row = sum(1 for row in reader)
    return render_template('home_page.html', number = count_row)

@app.route('/movies/ratings/')
def show_six_movies():
    string = ""
    with open("movies_clean.csv","r", encoding = 'utf8') as f:
        reader = csv.reader(f)
        csv_list = list(reader)
        for i in range(6):
            a_tuple = csv_list[random.randint(1, len(csv_list) - 1)]
            string = string + str(Movie(a_tuple)) + ' <br> '
    return render_template('movies_ratings.html', string = string)

if __name__ == '__main__':
    app.run()
