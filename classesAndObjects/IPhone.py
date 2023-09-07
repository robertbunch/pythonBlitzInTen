from Phone import Phone

#An iPhone IS ALWAYS a phone
#How do we make this a subclass of Phone?
#we want the methods and attributes that Phones have
#we pass the parent/super class to the ()
class IPhone(Phone):
    def __init__(self):
        self.os = "iOS"
        self.make = "Apple"
    def open_facetime(self):
        print("Opening Facetime...")