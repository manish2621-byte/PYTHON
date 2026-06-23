'''Use ChatGPT to generate a Python example where a base class Notification has a send() method, and two subclasses (EmailNotification, SMSNotification) override send() to print different messages. Paste the generated code, run it, and write one line explaining how method overriding works in your example.'''

# Base Class
class Notification:
    def send(self):
        print("Sending a notification")

# Subclass 1
class EmailNotification(Notification):
    def send(self):
        print("Sending an email notification")

# Subclass 2
class SMSNotification(Notification):
    def send(self):
        print("Sending an SMS notification")

# Create objects
email = EmailNotification()
sms = SMSNotification()

# Call send() methods
email.send()
sms.send()
