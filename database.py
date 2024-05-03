import json
import os

class JsonDB:
    def __init__(self, filename):
        self.filename = filename
        self.data = self.load_data()

    def load_data(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'r') as f:
                return json.load(f)
        else:
            return []

    def create(self, dictionary):
        self.data.append(dictionary)
        self.save_data()

    def read(self, key=None) -> dict | None:
        if key is None:
            return self.data
        else:
            for dictionary in self.data:
                if key in dictionary:
                    return dictionary
            return None

    def update(self, key, dictionary):
        for i, d in enumerate(self.data):
            if key in d:
                self.data[i] = dictionary
                self.save_data()
                return
        raise KeyError(f"Key '{key}' not found")

    def delete(self, key):
        for i, d in enumerate(self.data):
            if key in d:
                del self.data[i]
                self.save_data()
                return
        raise KeyError(f"Key '{key}' not found")

    def save_data(self):
        with open(self.filename, 'w') as f:
            json.dump(self.data, f, indent=4)

