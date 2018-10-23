from flask import Flask, request,jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://Sahil:1234@localhost:27017/connect_to_mongo'


mongo = PyMongo(app)

@app.route('/create',methods =['POST'])
def create():
	prac = mongo.db.practice
	name = request.json['name']
	age = request.json['age']
	mobile = request.json['mobileno']

	pr = prac.insert({'name': name ,'age' : age , 'mobileno' : mobile})
	#User inserted in database

	new_user = prac.find_one({'_id' : pr})
	#user is searched to show in the Postman,the user is id is found & then the user details is put in new_user

	output = {'name' : new_user['name'],'age' : new_user['age'],'mobileno' : new_user['mobileno']}

	return jsonify({'result' : output})
	print "success"

@app.route('/a_data',methods =['GET'])
def a_data():
	prac = mongo.db.practice
	print 'started'
	response = []
	ex = prac.find({'name' : 'a'})
	for x in ex:
		print 'each data',x
		response.append({

				'name' : x['name'],
				'age' : x['age'],
				'mobileno' : x['mobileno']
			})

	print 'loop end'

	return jsonify(response)

@app.route('/age_21',methods =['GET'])
def age_21():
	prac = mongo.db.practice
	print 'start'
	response = []
	ex = prac.find({'age' : 21})
	for x in ex:
		print 'each data',x
		response.append({

				'name' : x['name'],
				'age' : x['age'],
				'mobileno' : x['mobileno']
			})

	print 'loop end'

	return jsonify(response)

if __name__ == '__main__' :
	app.run(debug=True)
