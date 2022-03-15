from flask import render_template, redirect, session, request, flash
from flask_app import app

#Modelo de Recipe
from flask_app.models.user import User

@app.route("/new/recipe")
def new_recipe():
    return render_template('new_recipe.html')