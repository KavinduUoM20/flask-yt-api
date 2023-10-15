from flask import Flask
from flask_restful import Api,Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):

    names = {"Kavindu":{"Age":23,"Town":"Kekirawa"},
             "Yasida": {"Age": 23, "Town": "Panadura"}}
    def get(self,name):
        if name in self.names:
            return self.names[name]
        else:
            return {"error": "Name not found"}, 404

api.add_resource(HelloWorld,"/hello/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
