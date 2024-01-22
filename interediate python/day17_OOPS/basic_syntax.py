class insta_user():
    def __init__(self, user_id, user_password):
        self.id = user_id
        self.password = user_password
        self.followers = 0
        self.following = 0

    def follows(self, user):
        self.following += 1
        user.followers += 1

user1 = insta_user("zoya28", 1234)
user2 = insta_user("hamza", 57594)

user1.follows(user2)
print(user1.following)