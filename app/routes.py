from flask import render_template, url_for, redirect, flash, request, abort
from app import app, db_app, bycrypt
from flask_login import login_user, logout_user, current_user, login_required
import secrets
import os

#REDERIZA O SITE INSTITUCIONAL
@app.route("/")
def site_institucional():
    return render_template("index.html")

@app.route("/contato")
def contato():
    return render_template("contato.html")