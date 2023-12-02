# class User:
#     pass  # pass vermeidet Fahler
# user_1 = User()

# # creating a attributes from outsite the class
# user_1.userName="nour"
# user_1.passWord="halloword"
# print(user_1.userName)
class User:
    def __init__(self, username, id, password):
        self.username = username
        self.id = id
        self.password = password

    def ausgabe(self):
        print(self.username)


user_1 = User("mrx", 1, "test")

user_1.ausgabe()
