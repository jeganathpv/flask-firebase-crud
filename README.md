# flask-firebase-crud
Flask App with Firebase connectivity 
    - Firebase Setup 
    - Firebase default app initialization
    - CRUD Operations using ToDo collection
    - Flask Setup & APIs to do crud operations

# Create APP on Firebase
    - Create Realtime database
    - Generate API Key (Python)
    - Put it on working directory (Also add the file to .gitignore)

# Install firebase-admin
    - pip install firebase-admin

# Install flask modules
    - pip install flask
    - pip install flask-restful
    - pip install flask-cors

# Appsettings File
    I have use appsettings.json file to store configuration items
        - DatabaseURL
        - Collection Details

## [firebase_service.py](https://github.com/jeganathpv/flask-firebase-crud/blob/main/firebase_service.py)

This file contains connectivity of Firebase and sample CRUD operations using TODO List
    - Class ToDoCollection()
    - Initialize reference for `todo` collection
    
Methods | Description | Input | Output | Access
--- | --- | --- | --- | ---
`_getSnapshot()` | To get snapshot of collection | None | `dict` or `None` | Private
`__findItem(id)` | To find the item | id: 1 | `dict` or `False` | Private
`addTodoItem(content)` | To push/add new todo items into collection | dict: `{'id':1, 'task':'Task'}` | `Boolean` | Public
`getTodoItems()` | To get the entire todo items list | None | `list` | Public
`getTodoItem()` | To get the todo item | id: 1 | `dict` or `None` | Public
`clearAllItems()` | To clear all nodes in the collection | None | `Boolean` | Public
`updateTodoItem(self, id, content)` | To update item from the collection | id: 1, dict: `{'id':1, 'task':'Task'}` | `Boolean` | Public
`deleteTodoItem(id)` | To delete item from the collection | id: 1 | `Boolean` | Public

## [app.py](https://github.com/jeganathpv/flask-firebase-crud/blob/main/app.py)

Main python file run as Flask Restful API application

    - Added CORS Policy to the Flask App
    - Created APIs as Restful
    
# APIs Used in app.py - Flask Application

API URL | Description | METHOD | Body Content(Eg.) 
--- | --- | :---: | ---
*/health* | Check whether the application is running properly or not | **GET** | `None` 
*/getAllItems* | Return all the todo items | **GET** | `None`
*/getItem* | Return the todo item  | **POST** | `{"id": 1}`
*/addItem* | Add new todo item to the collection | **POST** | `{"id": 1 , "task": "My Todo task"}`
*/deleteItem* | Delete todo item from the collection | **DELETE** | `{"id": 1}`
*/deleteAllItems* | Delete all the items from the collection | **DELETE** |` None`
*/updateItem* | Delete all the items from the collection | **POST** | `{"id": 1 , "task": "My Todo task"}`

    - Success API call will have status code of 200
    - Failure and exception API with return with status code 400
    
## Thanks everyone





