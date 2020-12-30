import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path
if path.exists("env.py"):
    import env 

app = Flask(__name__)    

app.config['MONGO_URI'] = os.environ.get('MONGO_URI')
mongo = PyMongo(app)


@app.route('/')
@app.route('/home')
def home():
    """
    Renders the home page for user
    """
    return render_template('pages/home.html')

@app.route('/about')
def about():
    """
    Renders the about page for user
    """
    return render_template('pages/about.html', title='About', skills=mongo.db.skills.find())

@app.route('/projects')
def projects():
    """
    Renders the projects page for user
    """
    return render_template('pages/projects.html', title='Projects')

@app.route('/contact')
def contact():
    """
    Renders the contact page for user
    """
    return render_template('pages/contact.html', title='Contact')

@app.route('/admin')
def admin():
    """
    Renders the admin page for user
    """
    return render_template('pages/admin.html', title='Admin', skills=mongo.db.skills.find())

@app.route('/insertskill', methods=['POST'])
def insertskill():
    """
    Adds a skill to the database
    """
    skills = mongo.db.skills
    skills.insert_one(request.form.to_dict())
    return redirect(url_for('admin'))

@app.route('/addskill')
def addskill():
    """
    Renders the add skills page for user
    """
    return render_template('pages/addskill.html', title='Admin - Add Skill')

@app.route('/editskill/<skill_id>')
def editskill(skill_id):
    """
    Renders the edit skills page for user
    """
    the_skill = mongo.db.skills.find_one({"_id": ObjectId(skill_id)})
    all_skills = mongo.db.skills.find()
    return render_template('pages/editskill.html', skill=the_skill, skills=all_skills, title='Admin - Edit Skill')   

@app.route('/updateskill/<skill_id>', methods=["POST"])
def updateskill(skill_id):
    """
    Updates a skill to the database
    """
    skills = mongo.db.skills
    skills.update( {'_id': ObjectId(skill_id)},
    {
        'skill':request.form.get('skill'),
        'level':request.form.get('level')
    })
    return redirect(url_for('admin'))
    
@app.route('/deleteskill/<skill_id>')
def deleteskill(skill_id):
    """
    Deletes a skill from the database
    """
    mongo.db.skills.remove({'_id': ObjectId(skill_id)})
    return redirect(url_for('admin'))

if __name__ == '__main__':
    app.run(host=os.getenv('IP', '0.0.0.0'), 
    port=int(os.getenv('PORT', 8080)), 
    debug=True)