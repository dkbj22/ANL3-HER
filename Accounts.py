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
            nameset = input("Enter your nameset: ")
            surename = input("Enter your Surname: ")
            streetAddress = input("Enter your street address: ")
            zipcode = input("Enter your zip code: ")
            city = input("Enter your city: ")
            phoneNumber = input("Enter Your phonenumber: ")
            emailAddress = input("Enter Your Email: ")
            username = ""
            while len(username) == 0:
                username = input("Enter Your Username: ")
            allUserInfo = {"Gender" : gender, 
                            "NameSet" : nameset,
                            "GivenName" : name, 
                            "Surname" : surename, 
                            "StreetAddress" : streetAddress, 
                            "ZipCode" : zipcode, 
                            "City" : city, 
                            "EmailAddress" : emailAddress, 
                            "Username" : username, 
                            "TelephoneNumber" : phoneNumber, 
                            "Type" : type}
            jsonFile.append(allUserInfo) 
        with open(filePath, "w") as file:
            json.dump(jsonFile, file, indent=4)
            return username
    
    def Loginchecker(self, loginUsername):
        filePath = "AllAccounts.json"
        with open(filePath) as file:
            data = json.load(file)
            temp = data
            for account in temp:
                if account["Username"] == loginUsername[0]:
                    return account["Type"]
            return False  