class Notification:
    def send(self):
        print("Sending notification.")

class EmailNotification(Notification):
    def send(self):
        print("Sending email notification.")

class SMSNotification(Notification):
    def send(self):
        print("Sending SMS notification.")

class PushNotification(Notification):
    def send(self):
        print("Sending push notification.")

for notification in [EmailNotification(), SMSNotification(), PushNotification()]:
    notification.send()
