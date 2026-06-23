'''Create a class InstaStory with a method share() that prints 'Sharing an image story'. Now create another class WhatsAppStory that overrides share() to print 'Sharing a text status'. Instantiate both and call share() to show method overriding in action.'''

# Parent Class
class InstaStory:
    def share(self):
        print("Sharing an image story")

# Child Class (Method Overriding)
class WhatsAppStory(InstaStory):
    def share(self):
        print("Sharing a text status")

# Create objects
insta = InstaStory()
whatsapp = WhatsAppStory()

# Call share() method
insta.share()
whatsapp.share()

