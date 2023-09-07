from Phone import Phone

#An iPhone IS ALWAYS a phone
#How do we make this a subclass of Phone?
#we want the methods and attributes that Phones have
#we pass the parent/super class to the ()
class IPhone(Phone):
    def __init__(self,model,carrier,contacts):
        self.os = "iOS"
        self.make = "Apple"
        #super is a built in function to Python
        #super = the parent class 
        super().__init__(self.make,model,carrier,self.os,contacts)
    def open_facetime(self):
        print("Opening Facetime...")