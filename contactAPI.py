# Importing flask module in the project is mandatory
# An object of Flask class is our WSGI application.
from flask import Flask, request
from createDB import Database
from contentGen import ContentGenerator
import json
import time

db = Database()
generator = ContentGenerator()
 
# Flask constructor takes the name of 
# current module (__name__) as argument.
app = Flask(__name__)
 
# The route() function of the Flask class is a decorator, 
# which tells the application which URL should call 
# the associated function.

@app.route('/')
def hello_world():
    return 'Hello World'

@app.route('/refresh')
def refresh():
    db.refreshDatabase()
    return 'Done!' #Should refresh database with most up to date info

@app.route('/lookup')
def lookup():
    name = request.args.get('name')
    party = request.args.get('party')
    state = request.args.get('state')
    office = request.args.get('office')
    return db.getAll(name=name, party=party,state=state,office=office)

@app.route('/senate')
def senate():
    return db.getAll(office="senator")

@app.route('/governors')
def governors():
    return db.getAll(office='governor')

@app.route('/executive')
def executive():
    return db.getAll(office='whitehouse')

@app.route('/house')
def house():
    return db.getAll(office='representative')

@app.route('/candidates')
def candidates():
    return db.getAll(office='candidate')


@app.route('/generateEmail', methods=['POST']) #Example Post: Invoke-RestMethod -Method POST -Uri "http://127.0.0.1:5000/generateEmail" -Body ('{"type" : "bill","issue" : "the TikTok Ban Bill","title" : "Senator","name" : "Alex Padilla","support" : "oppose","description" : "I am an avid user of the app and do not want to see it banned","userInfo" : "IceCoffey\n123 Address Way\nCity, STATE"}' | ConvertTo-Json) -ContentType 'application/json'
def email():
    dataStr = request.get_json()
    data = json.loads(dataStr)
    type = data['type']
    issue = data['issue']
    title = data['title']
    name = data['name']
    support = data['support']
    description = data['description']
    userInfo = data['userInfo']
    return generator.generateEmail(
        type=type,
        issue=issue,
        title=title,
        name=name,
        support=support,
        description=description,
        userInfo=userInfo
    )

@app.route('/generatePhone', methods=['POST']) #Example Post: Invoke-RestMethod -Method POST -Uri "http://127.0.0.1:5000/generatePhone" -Body ('{"type" : "bill","username" : "Zach Efron","title" : "Senator","name" : "Alex Padilla","state" : "California","support" : "opposition","issue" : "the TikTok Ban Bill","description" : "I am an avid user of the app and do not want to see it banned"}' | ConvertTo-Json) -ContentType 'application/json'
def call():
    dataStr = request.get_json()
    data = json.loads(dataStr)
    type = data['type']
    username = data['username']
    title = data['title']
    name = data['name']
    state = data['state']
    support = data['support']
    issue = data['issue']
    description = data['description']
    return generator.generatePhone(
        type=type,
        username=username,
        title=title,
        name=name,
        state=state,
        support=support,
        issue=issue,
        description=description
    )
 
# main driver function
if __name__ == '__main__':
 
    # run() method of Flask class runs the application 
    # on the local development server.
    app.run()