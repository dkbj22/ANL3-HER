import json 
import collections

class Account:
    def __init__(self):
        self.gender = ""
        self.name = ""
        self.surename = ""
        self.streetAddress = ""
        self.zipcode = ""
        self.city = ""
        self.phoneNumber = ""
        self.emailAddress = ""
        self.username = ""
        self.userRoll = ""
    #@staticmethod
    def Register(self, type):
        filePath = "AllAccounts.json"
        with open (filePath) as lib:
            jsonFile = json.load(lib)
            gender = input("Enter your gender: ")
            name = input("Enter your first name: ")
            surename = input("Enter your Surname: ")
            streetAddress = input("Enter your street address: ")
            zipcode = input("Enter your zip code: ")
            city = input("Enter your city: ")
            phoneNumber = input("Enter Your phonenumber: ")
            emailAddress = input("Enter Your Email: ")
            username = input("Enter Your Username: ")
            allUserInfo = {"Gender" : gender, 
                            "Name" : name, 
                            "Surname" : surename, 
                            "Street Address" : streetAddress, 
                            "Zip Code" : zipcode, 
                            "City" : city, 
                            "TelephoneNumber" : phoneNumber, 
                            "Email" : emailAddress, 
                            "Username" : username, 
                            "Type" : type}
            jsonFile.append(allUserInfo) 
        with open(filePath, "w") as file:
            json.dump(jsonFile, file, indent=4)