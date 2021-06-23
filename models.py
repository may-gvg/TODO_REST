import json

from flask import Flask

app = Flask(__name__)



class Todos:
    def __init__(self):
        try:
            with open("todos.json", "r") as f:
                self.todos = {}
                jsonobj = json.load(f)
                print(jsonobj)
                for item in jsonobj:
                    id = item['id']
                    print(id)
                    self.todos[id] = item
                print(self.todos)
        except FileNotFoundError:
            self.todos = {}

    def all(self):
        lista = []
        for key in self.todos:
            lista.append(self.todos[key])
        return lista

    def get(self, id):
        return self.todos[id]

    def create(self, data, id):
        data['id'] = id
        self.todos[id] = data
        self.save_all()

    def save_all(self):
        with open("todos.json", "w") as f:
            json.dump(self.all(), f)

    def update(self, id, data):
        data.pop('csrf_token')
        self.todos[id] = data
        self.save_all()

    def delete(self, id):
        todo = self.get(id)
        if todo:
            del(self.todos[id])
            self.save_all()
            return True
        return False

    def new_id(self):
        keys = self.todos.keys()
        if keys:
            m = max(keys)
        else:
            return 1
        return m + 1



todos = Todos()

if __name__ == '__main__':
    app.run()