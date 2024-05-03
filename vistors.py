import database
class Vistor:
    def __init__(self, name, age, email, password, phno, orders=[]) -> None:
        self.data = {
            "name" : name,
            "age" : age,
            "email" : email,
            "password" : password,
            "phno" : phno,
            "orders": orders,
        }
        self.__create_user()

    def __create_user(self):
        db = database.JsonDB("data.json")
        data = db.read("visitors")
        if data == None:
            db.create({"visitors" : {}})
        data = db.read("visitors")
        data["visitors"].update({self.data["name"] : self.data})
        db.update("visitors", data)

    def update_user(self):
        key = input("update : ")
        value = input("new value : ")
        if (key == "name"):
            print("can't change name as it is id of user")
        db = database.JsonDB("data.json")
        data = db.read("visitors")
        data["visitors"][self.data["name"]][key] = value
        self.data[key] = value
        db.update("visitors", data)
        db.save_data()

    def delete_user(self):
        db = database.JsonDB("data.json")
        data = db.read("visitors")
        data["visitors"].pop(self.data["name"])
        db.update("visitors", data)
        db.save_data()
    
    def user_details(self):
        return self.data
    
    def save_user(self):
        db = database.JsonDB("data.json")
        data = db.read("visitors")
        data["visitors"][self.data["name"]] = self.data 
        db.update("visitors", data)
        db.save_data()

    def update_orders(self, orders):
        db = database.JsonDB("data.json")
        data = db.read("visitors")
        data["visitors"][self.data["name"]]["orders"] += [orders]
        db.update("visitors", data)
        db.save_data()
    
    @staticmethod
    def get_user(name):
        db = database.JsonDB("data.json")
        data = db.read("visitors")
        if data == None or name not in data["visitors"].keys():
            return None
        user_data = data["visitors"][name]
        return Vistor(user_data["name"], user_data["age"], user_data["email"], user_data["password"], user_data["phno"], user_data["orders"])
        