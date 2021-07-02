import csv
import json
import random

class publicLibrary():
    def __init__(self):
        self.AllBooks =[]
        self.AllAccounts =[]

    def ImportBooks(self):
        checkImpBook = True
        try: 
            with open("Books.json") as f:
                for i in json.load(f):
                    self.AllBooks.append(i)
        except Exception:
            pass
        filePath = input("Enter file path: ")
        try: 
            with open (filePath) as getdata:
                data = json.load(getdata)
                ISBN = ""
                for book in data:
                    for i in range(0, 9):
                        ISBN += str(random.randrange(10))
                        if i == 2 or i == 5:
                            ISBN += "-"
                    self.AllBooks.append(book)
                    book["ISBN"] = ISBN
                    book["Available"] = 1
                    ISBN = ""
                
        except FileNotFoundError:
            print(' \n'*20)
            print('\033[H\033[J', end='') 
            print("File not found")
            input("Press any key to return: ")
            checkImpBook = False
        if checkImpBook == True:
            publicLibrary().addToJson(self.AllBooks)
            print("Books have been Imported")
            input("Press any key to return: ")

    def addToJson(self, book):
        with open("Books.json", 'w') as file:
            json.dump(book, file, indent=4)
            
    def ImportSubs(self):
        # csv_rows = []
        checkImpSub = True
        file = input("Enter your file path: ")
        with open("AllAccounts.json") as f:
            for i in json.load(f):
                self.AllAccounts.append(i)
        try: 
            with open(file) as csvfile:
                reader = csv.DictReader(csvfile)
                field = reader.fieldnames
                for row in reader:
                    a = {field[i]:row[field[i]] for i in range(len(field))}
                    self.AllAccounts.append(a)
                for i in self.AllAccounts:
                    d = i
                    try:
                        d["Type"] = d.pop("Number")
                    except:
                        pass
                    if d["Type"] != "Librarian" and d["Type"] != "Publisher":
                        d["Type"] = "Subscriber"
        except Exception:
            print(' \n'*20)
            print('\033[H\033[J', end='') 
            print("File not found")
            input("Press any key to return: ")
            checkImpSub = False
        if checkImpSub:
            publicLibrary().convert_write_json(self.AllAccounts)
            print("Subscribers have been Imported")
            input("Press any key to return: ")
            
            
    def convert_write_json(self, data):
        with open('Accounts.json', "w") as f:
            f.write(json.dumps(data, sort_keys=False, indent=2, separators=(',', ': ')))

class Backup():
    def backups(self, Func):
        jsonFiles = ["AllAccounts.json", "Books.json", "LoanAdministration.json"]
        backupFiles = ["backupAccounts.json", "backupBooks.json", "backupLoanAdministration.json"]
        fromFile = jsonFiles
        toFile = backupFiles
        backupCheck = True
        if Func == 2:
            fromFile = backupFiles
            toFile = jsonFiles
        
        try: 
            for i in range(0, len(jsonFiles)):
                with open(fromFile[i], "r") as From, open(toFile[i], "w") as to:
                        to.write(From.read())
        except Exception:
            backupCheck = False
            if Func == 1:
                print("There seems to be some files missing")
            elif Func == 2:
                print("There is no backup to restore from")
            input("Press any key to return to menu: ")
        if backupCheck == True:
            if Func == 1:
                print("Backup Succesfully Made")
            elif Func == 2:
                print("Backup Succesfully Restored")
            input("Press any key to return: ")