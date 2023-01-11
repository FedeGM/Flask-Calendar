import logging
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def welcome():
    return render_template('layout.html')

@app.route('/calendar')
def calendar():
    return render_template('calendar.html')