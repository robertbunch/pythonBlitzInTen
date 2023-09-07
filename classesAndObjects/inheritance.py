from Phone import Phone
from IPhone import IPhone

#inheritance - is a way in Python to allow one class
#to have all the methods and attributes of another

jims_phone = Phone('Apple','iphone 9','Verizon',"iOS",["Jamie"])
cedrics_phone = Phone('Google','Pixel 7 Pro','EE',"Android",["Sherlock","Marie"])
ravis_phone = IPhone("iphone 13",'Vodaphone',[])

print(jims_phone.make)
print(jims_phone.contacts)
cedrics_phone.call_first_contact()
print(ravis_phone.os)
print(ravis_phone.make)
print("Calling contact from Ravis phone...")
ravis_phone.call_first_contact()
print(ravis_phone.carrier)

ravis_phone.open_facetime()
# jims_phone.open_facetime()