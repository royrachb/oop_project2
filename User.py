from PostFactory import PostFactory

class User:
    def __init__(self, SocialNet, Name, Pass):
        self.Followers = []
        self._Name = Name
        self._Pass = Pass
        self.SocialNetwork = SocialNet
        self.online = True
        self.notifications = []
        self._post = []

    def follow(self, user):
        if self.online:
            if self not in user.Followers:
                user.Followers.append(self)
                print(f"{self._Name} started following {user.get_name()}")
            else:
                print(f"{self._Name} is already following {user.get_name()}")
        else:
            print("User is not online. Cannot follow.")

    def unfollow(self, user):
        if self.online:
            if self in user.Followers:
                user.Followers.remove(self)
                print(f"{self._Name} unfollowed {user.get_name()}")
        else:
            print("User is not online. Cannot unfollow.")

    def publish_post(self, post_type, *post_data):
        if self.online:
            factory = PostFactory()
            post = factory.create_post(self, post_type, *post_data)
            self._post.append(post)
            # Do something with the post, like storing it or displaying it
            post.print_post()
            self.SocialNetwork.notify("post", self, "")
            return post
        else:
            print("User is not online. Cannot publish post.")

    def __str__(self):
        return f"User name: {self._Name}, Number of posts: {len(self._post)}, Number of followers: {len(self.Followers)}"

    def get_name(self):
        return self._Name

    def get_Pass(self):
        return self._Pass

    def print_notifications(self):
        print(f"{self.get_name()}'s notifications:")
        for note in self.notifications:
            print(note)
