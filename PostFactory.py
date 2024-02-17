from PostTypes import TextPost, ImagePost, SalePost


class PostFactory:
    def create_post(self, User, post_type, *post_data):
        if post_type == "Text":
            return TextPost(User, *post_data)
        elif post_type == "Image":
            return ImagePost(User, *post_data)
        elif post_type == "Sale":
            return SalePost(User, *post_data)
        else:
            raise ValueError("Invalid post type: {}".format(post_type))
