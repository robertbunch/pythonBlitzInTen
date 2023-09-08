
class Customer():
    def __init__(self,make,model,carrier,os,contacts):
        print("Phone class __init__ running")
        self.make = make
        self.model = model
        self.carrier = carrier
        self.os = os
        self.contacts = contacts

    def call_first_contact(self):   
        print("Calling first contact...")
    def open_app_store(self):
        print("Opening the app store...")