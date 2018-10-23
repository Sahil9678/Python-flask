from flask import Flask, request,jsonify
from flask_pymongo import PyMongo
from pymongo import MongoClient

app = Flask(__name__)


app.config['MONGO_DBNAME'] = 'connect_to_mongo'
app.config['MONGO_URI'] = 'mongodb://Sahil:1234@localhost:27017/connect_to_mongo'


mongo = PyMongo(app)

@app.route('/create',methods =['POST'])
def create():
	user = mongo.db.user
	name = request.json['name']
	age = request.json['age']
	designation = request.json['designation']
	personality = request.json['personality']

	ex = user.insert({'name':name,'age':age,'designation':designation,'personality':personality})
	#yaha tak jo objectid h wo create ho chuki h, or data insert ho chuka h in the mongodb database.

	#ab agar hame ye jo objectid(yani ki name,age,designation,personality)postman ki output me show karni h,
	#to hame us id ko find karna hoga using find_one, or find_one hame us id ka data uski natural form(yani 
	#ki jis form me data store hua h)me provide kr dega.Or ye data jayega new_user ke pass.
	new_user = user.find_one({'_id': ex })


	#ab new_user is data ko daal dega output me using 'field1 = dict['field']'.
	output = {'name' : new_user['name'],'age' : new_user['age'],'designation' : new_user['designation'],'personality' : new_user['personality']}

	#ye data jayega result me , or is data ko json form me convert kr dega jsonify or return kr dega.
	return jsonify ({'result' :output})

	return 'Added User!'

@app.route('/find',methods=['GET'])
def find():
	user = mongo.db.users
	print 'started'
	response = []
	ex = user.find()
	for x in ex:
		print 'this--------------', x
		response.append(
              {
              	'first_name':x['name'] 
              }
			)
	print 'loop end'

	
	return jsonify(response)


@app.route('/update',methods=['POST'])
def update():
	user = mongo.db.users
	name = request.json['name']
	age = request.json['age']
	designation = request.json['designation']
	personality = request.json['personality']

	x =user.find_one({'name' : name})
	
	ex = user.update({'name':name},{'age':age,'designation':designation,'personality':personality})

	user.save(ex)
	return 'Updated Walden!'

@app.route('/delete',methods=['POST'])
def delete():
	user = mongo.db.users
	name = request.json['name']
	ex = user.find_one({'name' : name})
	user.remove(ex)
	return 'REmoved Walden!!'

if __name__ == '__main__' :
	app.run(debug=True)
