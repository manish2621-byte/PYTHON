'''Write a Python class called InstagramPost with attributes caption, likes, and comments (a list). Add a method add_comment(comment_text) that appends a new comment to the comments list and increases the likes by 1.'''

class InstagramPost:
    def __init__(self, caption, likes, comments):
        self.caption = caption
        self.likes = likes
        self.comments = comments

    def add_comment(self, comment_text):
        self.comments.append(comment_text)
        self.likes += 1

    def show_post(self):
        print("Caption:", self.caption)
        print("Likes:", self.likes)
        print("Comments:", self.comments)


# Creating an Instagram post object
post = InstagramPost(
    "Enjoying the beautiful sunset! 🌅",
    100,
    ["Amazing view!", "So beautiful!"]
)

# Adding a new comment
post.add_comment("Wonderful picture!")

# Displaying updated post details
post.show_post()