from flask import Flask ,jsonify,request,json
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy.sql import func
from sqlalchemy import Column , DateTime

app = Flask(__name__)

x = 'mysql+pymysql://root:python123@localhost:3306/newdb'
app.config['SQLALCHEMY_DATABASE_URI'] = x
app.config['SQLALCHEMY_TRACK_MODIFICATIONS_'] = False 

db = SQLAlchemy(app)

class school(db.Model):
	id = db.Column(db.Integer,primary_key=True)
	name =db.Column(db.String(25))
	age = db.Column(db.Integer)
	grade = db.Column(db.String(25))

@app.route('/create',methods=['POST'])
def create():
	print 'start create'

	name = request.json['name']
	age = request.json['age']
	grade = request.json['grade']

	info = school(name = name,age= age,grade=grade)
	print info

	db.session.add(info)
	db.session.commit()

	print 'Success'
	return 'Success'

if __name__ == '__main__':
	app.run(debug=True)
