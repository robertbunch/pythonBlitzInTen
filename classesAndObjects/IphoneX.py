from IPhone import IPhone
#the iphoneX was the first iphone to use facial id
#the inheritance tree goes like this...
#Phone ---> IPhone ---> IPhoneX
class IPhoneX(IPhone):
    def __init__(self,carrier,contacts):
        self.facial_id = True
        #super is the parent class
        super().__init__('iPhoneX',carrier,contacts)

    #the same attribute with self, will be used instead of the method
    def run_facial_id(self):
        print("Running facial ID")