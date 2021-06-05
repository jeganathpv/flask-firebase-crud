# Import Firebase ToDo Collection
from firebase_service import ToDoCollection

# Import Modules for FLASK
from flask import Flask, jsonify, request
from flask_restful import Api, Resource
from flask_cors import CORS, cross_origin

# Initialize Flask app
app = Flask(__name__)
CORS(app, support_credentials=True)
api = Api(app)

class HealthCheck(Resource):
    @app.route('/health', methods=['GET'])
    @cross_origin(support_credentials=True)
    def checkHealth():
        return "Healthy"


class TodoItemsList(Resource):
    @app.route('/getAllItems', methods=['GET'])
    @cross_origin(support_credentials=True)
    def getAllItems():
        try:
            todoItems = todo.getTodoItems()
            return jsonify(todoItems)
        except Exception as ex:
            return str(ex)

class GetTodoItem(Resource):
    @app.route('/getItem', methods=['POST'])
    @cross_origin(support_credentials=True)
    def getItem():
        try:
            json_data = request.get_json(force=True)
            itemId = json_data['id']
            itemValue = todo.getTodoItem(itemId)
            return jsonify(itemValue)
        except Exception as ex:
            return str(ex)

if __name__ == "__main__":
    todo = ToDoCollection()
    api.add_resource(HealthCheck)
    api.add_resource(TodoItemsList)
    api.add_resource(GetTodoItem)
    app.run(debug=True) # Make sure debug is false on production environment