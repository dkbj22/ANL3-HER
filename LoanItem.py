from Account import Account
from LoadAdministration import loadAdministration
import json
from Books import books

class LoanItem():
    def __init__(self, LogInInfoLoan):
        self.LogInInfoLoan = LogInInfoLoan
        self.ISBN = ""
        self.Title = ""
        self.Author = ""
        self.Username = ""

    def loanItem(self):
        books.showAll_books(self)
        ISBN = input("Enter the ISBN of the book u want to loan or press x to cancel: ")

        filePath = "LoanAdministration.json"
        checkBook = False
        CheckWhile = True
        Cancel = False
        samebook = False
        while True:
            with open ("LoanAdministration.json") as check:
                checkdata = json.load(check)
                for j in checkdata["loanItems"]:
                    if j["ISBN"] == ISBN and j["Username"] == self.LogInInfoLoan:
                        print("U already have this book loaned")
                        samebook = True
                        ISBN = input("Enter the ISBN of the book u want to loan or press x to cancel: ")
                    else:
                        samebook = False
                if(samebook == False):
                    break
        if samebook == False:
            with open ("Books.json") as getdata:
                data = json.load(getdata)
                while CheckWhile:
                    if ISBN == "x":
                        Cancel = True
                        break
                    for i in data:
                        if i["ISBN"] == ISBN and i["Copies"] >= 1:
                            checkBook = True
                            Title = i["title"]
                            Author = i["author"]
                            CheckWhile = False
                            i["Copies"] = i["Copies"] -1
                    if checkBook == False:
                        print("This ISBN number does not exist or is unavailable")
                        ISBN = input("Enter the ISBN of the book u want to loan: ")
            if Cancel == False:
                with open('Books.json', 'w') as file:
                    json.dump(data, file, indent=2)
            if checkBook == True:
                with open (filePath) as loan:
                    data = json.load(loan)
                    temp = data["loanItems"]
                    y = {"Username" : self.LogInInfoLoan[0], "title" : Title, "ISBN" : ISBN, 
                        "author" : Author}
                    temp.append(y)
                    #safed book
                with open(filePath, "w") as f:
                    json.dump(data, f, indent=4)

    def ReturnLoanedItem(self):
        new_data = []
        test = loadAdministration(self.LogInInfoLoan)
        test.Inventory()
        ISBN = input("Enter the ISBN of the book u want to return or press x to cancel")
        ##Boek verwijderen deel
        with open("LoanAdministration.json", "r") as loan:
            data = json.load(loan)
        i = 0
        for check in data["loanItems"]:
            if check["ISBN"] == ISBN:
                del data["loanItems"][i]
            else:
                pass
            i += 1
        with open ("LoanAdministration.json", "w") as f:
            json.dump(data, f, indent=4)
        ##Boek updaten dat t beschikbaar is
        i = 0
        with open("Books.json", "r") as book:
            loanbook = json.load(book)
            for item in loanbook:
                if item["ISBN"] == ISBN:
                    loanbook[i]["Copies"]  = loanbook[i]["Copies"] + 1
                i += 1
        with open("Books.json", "w") as file:
            json.dump(loanbook, file, indent=4)
