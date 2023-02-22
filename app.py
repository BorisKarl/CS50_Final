import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from math import *
from datetime import *
from sys import *


# Configure application
app = Flask(__name__)



# Configure CS50 Library to use SQLite database
#db = SQL("sqlite:///namo.db")

@app.route("/")
def index():
    
    return render_template("index.html")
