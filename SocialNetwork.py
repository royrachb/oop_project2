from User import User


class SocialNetwork:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, name):
        if not hasattr(self, 'initialized'):
            self.NetworkName = name
            self.UserArray = []
            self.initialized = True
            print(f"The social network {name} was created!")

    def sign_up(self, username, password):
        # Check if username is already used
        for user in self.UserArray:
            if user.get_name() == username:
                print("Username already exists. Please choose a different one.")
                return None

        # Check password length
        if len(password) < 4 or len(password) > 8:
            print("Password must be between 4 and 8 characters long.")
            return None

        # Create a new user
        User1 = User(self, username, password)
        self.UserArray.append(User1)
        return User1

    def log_in(self, name, password):
        for user in self.UserArray:
            if user.get_name() == name:
                if user.get_Pass() == password:
                    user.online = True
                    print(f"{user.get_name()} connected")

    def log_out(self, name):
        for user in self.UserArray:
            if user.get_name() == name:
                user.online = False
                print(f"{user.get_name()} disconnected")

    def notify(self, MsgType, user, user2):
        if MsgType == "post":
            for user1 in self.UserArray:
                if user1.get_name() != user.get_name():
                    user1.notifications.append(f"{user.get_name()} has a new post")
        if MsgType == "comment":
            user.notifications.append(f"{user2.get_name()} commented on your post")

        if MsgType == "like":
            user.notifications.append(f"{user2.get_name()} liked your post")

    def __str__(self, netStr=None):
        netStr = f"{self.NetworkName} social network:\n"
        for user in self.UserArray:
            netStr += user.__str__() + "\n"
        return str(netStr)
