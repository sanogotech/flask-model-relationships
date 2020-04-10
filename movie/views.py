

from flask import Flask, render_template, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os, json
from . import app,db
from  .models import *


@app.route("/")
def hello():
    movie = db.session.query(Movie).first()
    return render_template("movie.html", movie=movie)


@app.route("/dyn/")
def dyn():
    return render_template("dynamic.html")


@app.route("/api/movies/", methods=['GET', 'POST'])
def movies_endpoint():
    if request.method == 'POST':
        m = Movie(title=request.form['title'])
        db.session.add(m)
        db.session.commit()
        return jsonify(m.to_json()), 201
    else:
        movies = db.session.query(Movie).all()
        return jsonify([m.to_json() for m in movies])


@app.route("/api/movies/<m_id>")
def movie_endpoint(m_id=None):
    if m_id:
        m = db.session.query(Movie).get(m_id)
        return jsonify(m.to_json())
    else:
        return abort(404)

