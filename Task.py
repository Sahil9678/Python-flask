from flask import Flask , jsonify , request , json ,flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from sqlalchemy import Column , DateTime

app = Flask(__name__)

x = 'mysql+pymysql://root:python123@localhost:3306/Cutter'
app.config['SQLALCHEMY_DATABASE_URI'] = x
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Ak47(db.Model):
	#ham class banate h taki hame fields mil jayein jo ki db se connected ho or ek id naam ki primary field banyenge 
	#taki ham uniquely kisi person ko identify kar sakein.
	id = db.Column(db.Integer , primary_key=True)
	name = db.Column(db.String(25))
	age = db.Column(db.Integer)
	designation = db.Column(db.String(30)) 
	personality = db.Column(db.String(50))

@app.route('/create',methods=['POST'])
def create():

	print 'create is working till now'

	#yaha ham json(yani dictionary form that is 'key':'value')form me 'name,age,designation,personality' request kar
	#rahe h ,so jab user post karega to is tarah se post karega:
	#{
	#	"name" : "Sahil",
	#	"age" :"21",
	#	"designation" : "Software Engineer",
	#	"personality" : "Good"
	#}
	name = request.json['name']
	age = request.json['age']
	desi = request.json['designation']
	per = request.json['personality']

	#iske baad ham jo value hame mili h usse variables me le lenge or class me insert kar denge.class me kyun insert 
	#karenge ? kyunki class is the only way to connect to database.so we will insert the variables value in the class
	#field so as to connect to database or ye sab value jayegi ek variable me .so basically jo bhi data ham post 
	#karenge wo "info" variable me jayega. Or is value ko ham add kar denge database ke ek session me.or using 
	#"db.session.commit" ham save kr denge database me.

	info= Ak47(name=name , age =age , designation =desi, personality =per)
	db.session.add(info)
	db.session.commit()

	return("Success")

@app.route('/read',methods=['GET'])
def read():
	print 'get method is called'
	response = []
	#ham sara data using "class.query.all()" get kar lenge or variable me daal denge. ab jo data h ,wo originally 
	#json(yani dictionary) form me h.So ham har data(yani ki har row of table) ko using "for" loop print kar denge.
	#puri list ko print karne ke liye ham ek dictionary banayenge or us dictionary me ye sara data yani ki har 
	#ek row ko append(add) kr denge. or print kr denge. or postman me print karne ke liye hame is dictionary ko 
	#jsonify karna padega.
	all_data = Ak47.query.all()	
	for data in all_data:
		print 'each data',data.name
		response.append({

			'id' : data.id,
			'name': data.name,
			'age': data.age,
			'designation': data.designation,
			'personality': data.personality
		
		})
	print 'response variable:', response

	return jsonify(response)

@app.route('/update',methods=['POST'])
def update():
	print 'update is working till now'

	#yaha ham json(yani dictionary form that is 'key':'value')form me 'name,age,designation,personality' request kar
	#rahe h ,so jab user post karega to is tarah se post karega:
	#{
	#	"name" : "Sahil",
	#	"age" :"21",
	#	"designation" : "Software Engineer",
	#	"personality" : "Good"
	#}
	new_name = request.json['name']
	new_age = request.json['age']
	new_designation = request.json['designation']
	new_personality =request.json['personality']

	#ye jo 'new_name' variable h ,iski value ham search karegein using "class.query.filter_by". or "first" hame  
	#jo pehla search result h wo provide kr dega.ye searched row h wo jayegi "obj" naam ke variable me.
	obj = Ak47.query.filter_by(name =new_name).first()

	#ab Agar hame row mil jata h to ham new_name ki value obj.name me daal denge or new_age ki value obj.age me & so
	#on. obj jisme already us sari row ki value padi h wo ham nayi value yani new_name,new_age & so on, se replace 
	#kar denge.  
	obj.name = new_name,
	obj.age = new_age,
	obj.designation = new_personality,
	obj.personality = new_designation

	db.session.commit()
	return 'success'

@app.route('/delete',methods=['POST'])
def delete():
	print 'delete is working till now'

	#yaha ham json(yani dictionary form that is 'key':'value')form me 'name' request kar rahe h ,so jab user post 
	#karega to is tarah se post karega:
	#{
	#	"name" : "Sahil"
	#}
	new_name = request.json['name']
	print new_name

	#ye jo 'new_name' variable h ,iski value ham search karegein using "class.query.filter_by".ye searched row h 
	#wo jayegi "obj" naam ke variable me.

	obj = Ak47.query.filter_by(name =new_name)
	#ye jo "obj" h ye kind of rows h,matlab kayi sari rows bhi ho sakti h ye(agar ham koi naam search karte h or
	# us naam ke kayi saare person ho database me , to sare same name ke bande is obj me aa jayenge),so if we 
	#want to access the names one by one than we use "for"   
	for f in obj:
		print f.age
		db.session.delete(f)
	
	db.session.commit()

	return 'Success'

if __name__ == '__main__':
    app.run(debug=True)
