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
        """
            checkHealth(): Check whether the service is working or not
        """
        return "Healthy"


class TodoItemsList(Resource):
    @app.route('/getAllItems', methods=['GET'])
    @cross_origin(support_credentials=True)
    def getAllItems():
        """
            getAllItems(): List all the todo items
        """
        try:
            todoItems = todo.getTodoItems()
            return jsonify(todoItems)
        except Exception as ex:
            return str(ex), 400

class GetTodoItem(Resource):
    @app.route('/getItem', methods=['POST'])
    @cross_origin(support_credentials=True)
    def getItem():
        """
            getItem(): Return the todo item 
            Ensure you pass a ID as part of json body in post request
            e.g. Request Body ={"id": 1}
        """
        try:
            json_data = request.get_json(force=True)
            itemId = json_data['id']
            itemValue = todo.getTodoItem(itemId)
            return jsonify(itemValue)
        except Exception as ex:
            return str(ex), 400

class AddToDoItem(Resource):
    @app.route('/addItem', methods=['POST'])
    @cross_origin(support_credentials=True)
    def addItem():
        """
            addItem(): Add new todo item to the collection
            Ensure you pass a ID, Task as part of json body in post request
            e.g. Request Body = {"id": 1 , "task": "My Todo task"}
        """
        try:
            json_data = request.get_json(force=True)
            itemValue = todo.addTodoItem(json_data)
            return jsonify(itemValue)
        except Exception as ex:
            return str(ex), 400

class DeleteToDoItem(Resource):
    @app.route('/deleteItem', methods=['DELETE'])
    @cross_origin(support_credentials=True)
    def deleteItem():
        """
            deleteItem(): Delete todo item from the collection
            Ensure you pass a ID as part of json body in post request
            e.g. Request Body = {"id": 1 }
        """
        try:
            json_data = request.get_json(force=True)
            itemId = json_data['id']
            status = todo.deleteTodoItem(itemId)
            return jsonify(status)
        except Exception as ex:
            return str(ex), 400

class DeleteAllToDoItems(Resource):
    @app.route('/deleteAllItems', methods=['DELETE'])
    @cross_origin(support_credentials=True)
    def deleteAll():
        """
            deleteAll(): Delete all the items from the collection
        """
        try:
            status = todo.clearAllItems()
            return jsonify(status)
        except Exception as ex:
            return str(ex), 400

class UpdateToDoItem(Resource):
    @app.route('/updateItem', methods=['POST'])
    @cross_origin(support_credentials=True)
    def updateItem():
        """
            updateItem(): Update existing todo item from the collection
            Ensure you pass a ID & Task as part of json body in post request
            e.g. Request Body = {"id": 1, "task": "My updated task" }
        """
        try:
            json_data = request.get_json(force=True)
            itemId = json_data['id']
            status = todo.updateTodoItem(itemId, json_data)
            return jsonify(status)
        except Exception as ex:
            return str(ex), 400

if __name__ == "__main__":
    todo = ToDoCollection()
    app.run(debug=True) # Make sure debug is false on production environment