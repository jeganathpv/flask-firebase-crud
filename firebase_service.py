# Import the Firebase service
import firebase_admin
from firebase_admin import credentials, db

# Other Modules
import json

# Load appsettings JSON file
with open('appsettings.json', 'r') as json_file:
    appsettings = json.load(json_file)

# Firebase-APIKey File
API_KEY_PATH = "firebase-api-key.json" #Add your API file path

# Initialize the default firebase app
certificate = credentials.Certificate(API_KEY_PATH) 
firebaseApp = firebase_admin.initialize_app(certificate, {'databaseURL': appsettings['DatabaseURL']})


class ToDoCollection():
    """Class to perform CRUD Operations with Firebase collection TODO"""

    def __init__(self):
        """ Collection reference for ToDo """
        self.collection = db.reference(appsettings['TodoCollection'])
        self.key = appsettings['TodoCollectionUniqueKey']
    
    def __getSnapshot(self):
        """ Private method, It can access within class object 
        To get snapshot of collection """
        return self.collection.get()
    
    def __findItem(self, id):
        """
            To find the item 
            """
        snapshot = self.__getSnapshot()
        if snapshot == None:
            return False
        item = None
        for key, val in snapshot.items():
            if val[self.key] == id:
                item = key
                break
        if(item != None):
            node = self.collection.child(item)
            return node
        else:
            return False

    def addTodoItem(self, content):
        """ To push/add new todo items into collection """
        if self.key in content:
            if not self.__findItem(content[self.key]):
                self.collection.push(content)
                return True
            else:
                raise Exception("Item already exists")
        else:
            raise Exception("Key {0} not found".format(self.key))

    def getTodoItems(self):
        """ To get the entire todo items list """
        snapshot = self.__getSnapshot()
        todos = []
        for key, val in snapshot.items():
            todos.append(val)
        return todos

    def getTodoItem(self,id):
        """ To get the todo item as dict which matches the id else return None """
        todoList = self.getTodoItems()
        todoItem = next((item for item in todoList if item[self.key] == id), None)
        return todoItem

    def clearAllItems(self):
        """ To clear all nodes in the collection"""
        self.collection.delete()
        return True

    def updateTodoItem(self, id, content):
        """ To update existing todo item 
            Return True 
            If the key is not found then return false
         """
        itemMatchedNode = self.__findItem(id)
        if(itemMatchedNode == False):
            raise Exception("Item doesn't exists")
        itemMatchedNode.set(content)
        return True

    def deleteTodoItem(self, id):
        """ To delete item from the list 
            Return True 
            If the key is not found then return false
         """
        itemMatchedNode = self.__findItem(id)
        if(itemMatchedNode == False):
            raise Exception("Item doesn't exists")
        itemMatchedNode.delete()
        return True