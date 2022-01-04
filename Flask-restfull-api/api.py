from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy


  
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///text.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    dob = db.Column(db.String(80), unique=True, nullable=False)
    def __init__(self,name, dob):
        self.name= name
        self.dob =dob

    def __repr__(self):
        return '<Name %r>' % self.name

api = Api(app)
class UsersList(Resource):
    def get(self):
        return jsonify([{
            "id": user.id, 'name':user.name, "dob":user.dob
            } for user in User.query.all()
            #for user in User.query.all()
        ])

class SingleUser(Resource):
    def get(self, num):
        user=User.query.filter_by(id=num).first_or_404()
        return jsonify([{
            "id": user.id, 'name':user.name, "dob":user.dob
        }])


class NewUser(Resource):
    def post(self):
        try:
            new_x = request.get_json()
            newuser=User(new_x['name'],new_x['dob'])
            db.session.add(newuser)
            db.session.commit()
            return {'message': 'POST data read successfully'}
        except:
            return {'message': 'Something went wrong'}

class deleteUser(Resource):
    def delete(self, num):
        try:
            todo = User.query.filter_by(id=num).first()
            db.session.delete(todo)
            db.session.commit()
            return {'message': 'User successfully deleted successfully'}
        except:
            return {'message': 'Something went wrong'}

# @app.route("/users/<int:id>", methods = ['PUT'])
# def put(id):
#     print("hello")
#     try:
#         UpUser=User.query.filter_by(id=id).first()
#         new_x = request.get_json()
#         if new_x['name']:
#             print(new_x['name'])
#             UpUser.name=new_x['name']
#         if new_x["dob"]:
#             print("hello2")
#             UpUser.dob =new_x['dob']
#         db.session.commit()
#         return {'message': 'POST data read successfully'}
#     except:
#         return {'message': 'Something went wrong'}

class UpdateUser(Resource):
    def put(self,id):
        print("hello")
        try:
            UpUser=User.query.filter_by(id=id).first()
            new_x = request.get_json()
            if new_x['name']:
                print(new_x['name'])
                UpUser.name=new_x['name']
            if new_x["dob"]:
                print("hello2")
                UpUser.dob =new_x['dob']
            db.session.commit()
            return {'message': 'Updated the data successfully'}
        except:
            return {'message': 'Something went wrong'}

    def patch(self,id):
        try:
            UpUser=User.query.filter_by(id=id).first()
            new_x = request.get_json()
            if new_x['name']:
                UpUser.name=new_x['name']
            if new_x["dob"]:
                UpUser.dob =new_x['dob']
            db.session.commit()
            return {'message': 'Updated the data successfully'}
        except:
            return {'message': 'Something went wrong'}

  
api.add_resource(UsersList, '/')
api.add_resource(SingleUser, '/<int:num>')
api.add_resource(NewUser, '/user')
api.add_resource(deleteUser,"/delete/<int:num>")
api.add_resource(UpdateUser,"/user/<int:id>")
 
# driver function
if __name__ == '__main__':
  
    app.run(debug = True)