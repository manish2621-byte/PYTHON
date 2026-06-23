'''Refactor your VerifiedInfluencer class to include a method display_profile() that prints details in the format used on Instagram profiles (username, followers in K/M, badge status).<br><br><em><strong>Hint:</strong> Use a helper function to format large follower counts, e.g., 1500 as '1.5K'.</em>'''

class User:
    def __init__(self, username, email):
        self.username = username
        self.email = email


class Influencer(User):
    def __init__(self, username, email, followers):
        super().__init__(username, email)
        self.followers = followers


class VerifiedInfluencer(Influencer):
    def __init__(self, username, email, followers, badge):
        super().__init__(username, email, followers)
        self.badge = badge

    # Helper function to format followers
    def format_followers(self):
        if self.followers >= 1_000_000:
            return f"{self.followers / 1_000_000:.1f}M"
        elif self.followers >= 1_000:
            return f"{self.followers / 1_000:.1f}K"
        else:
            return str(self.followers)

    # Display profile like Instagram
    def display_profile(self):
        print("===== Instagram Profile =====")
        print("Username:", self.username)
        print("Followers:", self.format_followers())
        print("Badge Status:", self.badge)
        print("============================")


# Create object
v1 = VerifiedInfluencer(
    "manishsharma",
    "manishsharma@gmail.com",
    1500,
    "Blue Tick"
)

# Display profile
v1.display_profile()