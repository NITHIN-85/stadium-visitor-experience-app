import visit
import vistors
import os

clear = lambda: os.system('clear')

class StadiumSupport:

    def __init__(self):

        while True:
            print("1. login")
            print("2. signup")
            print("3. exit")
            choice = int(input("enter your choice : "))
            if choice == 1:
                state = self.handleLogin() 
                if (state == "exited"):
                    return
            elif choice == 2:
                clear()
                self.handleSignup()
            elif choice == 3:
                return
            else:
                print("invalid choice")

    def handleLogin(self):
        clear()
        user_name = input("enter your username : ")
        password = input("enter your password : ")
        user = vistors.Vistor.get_user(user_name)
        if user == None:
            print("invalid user, Signup..!")
            return
        original_password = user.data["password"]
        if password == original_password:
            v = visit.Visit.get_visit(user_name, password)
            if v == None:
                v = visit.Visit(user_name, password)
            initial_login = True
            while True:
                clear()
                if (initial_login):
                    print("login successfull")
                    initial_login = False
                print("1. order food")
                print("2. book room")
                print("3. delete vistor")
                print("4. update user details")
                print("5. logout")
                print("6. exit stadium")
                choice = int(input("enter you choice : "))
                if choice == 1:
                    clear()
                    v.order_food()
                elif choice == 2:
                    clear()
                    v.book_room()
                elif choice == 3:
                    v.delete_visit()
                    user = vistors.Vistor.get_user(v.data["user"]["name"])
                    user.delete_user()
                    return "exited"
                elif choice == 4:
                    user = vistors.Vistor.get_user(v.data["user"]["name"])
                    user.update_user()
                elif choice == 5:
                    return
                elif choice == 6:
                    v.delete_visit()
                    return "exited"
                else:
                    print("invalid choice")
        else:
            print("invalid password")

    def handleSignup(self):
        # def __init__(self, name, age, email, password, phno, orders=[]) -> None:
        
        name = input("enter your name : ")
        user = vistors.Vistor.get_user(name)
        if user != None:
            print("user name already exists, consider adding numbers or special character")
            self.handleSignup()
        age = input("enter your age : ")
        phno = input("enter yoru phno : ")
        email = input("enter your email : ")
        password = input("enter your passowrd : ")
        vistors.Vistor(name, age, email, password, phno)

StadiumSupport()