from PIL import Image


class Post:
    Likes = 0
    CommentsArray = []

    def __init__(self, user):
        self.user = user

    def print_post(self):
        raise NotImplementedError("print_post method must be implemented in subclasses")

    def like(self, user):
        if user != self.user:
            self.Likes += 1
            print(f"notification to {self.user.get_name()}: {user.get_name()} liked your post")
            self.user.SocialNetwork.notify("like", self.user, user)

    def comment(self, user, data):
        self.CommentsArray.append(data)
        if user != self.user:
            print(f"notification to {self.user.get_name()}: {user.get_name()} commented on your post: {data}")
            self.user.SocialNetwork.notify("comment", self.user, user)


class TextPost(Post):
    def __init__(self, user, text_data):
        super().__init__(user)
        self.text_data = text_data

    def print_post(self):
        print(f"{self.user.get_name()} published a post:")
        print(f'"{self.text_data}"\n')

    def __str__(self):
        print_string = f"{self.user.get_name()} published a post:\n"
        print_string += f'"{self.text_data}"\n'
        return print_string


class ImagePost(Post):
    def __init__(self, user, image_data):
        super().__init__(user)
        self.image_data = image_data

    def print_post(self):
        print(f"{self.user.get_name()} posted a picture\n")

    def __str__(self):
        return f"{self.user.get_name()} posted a picture\n"

    def display(self):
        image = Image.open('image.jpg')
        image.show()
        print("Shows picture")


class SalePost(Post):
    def __init__(self, user, post_type, cost, place):
        super().__init__(user)
        self.post_type = post_type
        self.cost = cost
        self.place = place
        self.isSold = False

    def print_post(self):
        print(f"{self.user.get_name()} posted a product for sale:")
        print(f"For sale! {self.post_type}, price: {self.cost}, pickup from: {self.place}\n")

    def discount(self, percent, password):
        if password == self.user.get_Pass():
            self.cost = self.cost * (1 - (percent / 100))
            print(f"Discount on {self.user.get_name()} product! the new price is: {self.cost}")

    def __str__(self):
        if self.isSold:
            post_str = f"{self.user.get_name()} posted a product for sale:\n"
            post_str += f"Sold! {self.post_type}, price: {self.cost}, pickup from: {self.place}\n"
        else:
            post_str = f"{self.user.get_name()} posted a product for sale:\n"
            post_str += f"For sale! {self.post_type}, price: {self.cost}, pickup from: {self.place}\n"
        return post_str

    def sold(self, password):
        if password == self.user.get_Pass():
            self.isSold = True
            print(f"{self.user.get_name()}'s product is sold")
