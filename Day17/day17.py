class User:
    def __init__(self, user_id, username):  #initialize the class, every time using the class, this will be triggered
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


    def unfollow(self, user):
        user.followers -= 1
        self.following -= 1

   
user_1 = User("001", "Sunwoo")
user_2 = User("002", "Tjark")

print(user_1.followers) 

user_1.follow(user_2)

print(user_1.username) 
print(user_1.followers) 

