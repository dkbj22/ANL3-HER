import json

class catalog():
    def __init__(self):
        self.SearchTerm = ""
        self.BookFoundCheck = False
        self.OptionList = ["title","ISBN","author","alles"]
        self.OptionlistLoan = ["title","ISBN","author","Username","alles"]
    def SearchBook(self):
        OneRunCheck = True
        print("Enter the number of the option u would like to use for search: ")
        print("1. Title")
        print("2. ISBN")
        print("3. Author")
        print("4. Search on Title,ISBN and Author")
        print("5. Return")
        while True:
            while OneRunCheck:
                Choice = input("Enter number: ")
                try:
                    Choice = int(Choice)
                    OneRunCheck = False
                    break
                except ValueError:
                    print("please enter a valid number")
            if Choice >= 1 and Choice <= 5:
                if(Choice >= 1 and Choice <=4):
                    self.SearchTerm = input("Enter " + self.OptionList[Choice-1] + ": ")
                    self.BookFoundCheck = catalog.SearchBookKey(self,self.OptionList[Choice-1])
                    if self.BookFoundCheck == True:
                        print("Book was found")
                        break
                elif (Choice == 5):
                    break
                if (self.BookFoundCheck == False):
                    print("Book wasn't found")
                    break
            else:
                print("Please enter a valid number")
                OneRunCheck = True
        input("Press anykey to return: ")

    def SearchBookKey(self,SearchKey):
        with open ("Books.json") as getdata:
            data = json.load(getdata)
            if SearchKey == "alles":
                for book in data:
                    if(self.SearchTerm in book["title"] or self.SearchTerm in book["ISBN"] or self.SearchTerm in book["author"]):
                        self.BookFoundCheck = True
                        if(book["Copies"] >= 1):
                            print("Title: " + book["title"]  + " author: " + book["author"] + " ISBN: " + book['ISBN'] + " Book is currently: Available")
                        else:
                            print("Title: " + book["title"]  + " author: " + book["author"] + " ISBN: " + book['ISBN'] + " Book is currently: Unavailable")
            else:
                for book in data:
                    if(self.SearchTerm in book[SearchKey]):
                        self.BookFoundCheck = True
                        if(book["Copies"] >= 1):
                            print("Title: " + book["title"]  + " author: " + book["author"] + " ISBN: " + book['ISBN'] + " Book is currently: Available")
                        else:
                            print("Title: " + book["title"]  + " author: " + book["author"] + " ISBN: " + book['ISBN'] + " Book is currently: Unavailable")
            return self.BookFoundCheck
    
    def SearchLoanBook(self):
        OneRunCheck = True
        print("Enter the number of the option u would like to use for search: ")
        print("1. Title")
        print("2. ISBN")
        print("3. Author")
        print("4. Username")
        print("5. Search on Title,ISBN,Username and Author")
        print("6. Return")
        while True:
            while OneRunCheck:
                Choice = input("Enter number: ")
                try:
                    Choice = int(Choice)
                    OneRunCheck = False
                    break
                except ValueError:
                    print("please enter a valid number")
            if Choice >= 1 and Choice <= 6:
                if(Choice >= 1 and Choice <=5):
                    self.SearchTerm = input("Enter " + self.OptionlistLoan[Choice-1] + ": ")
                    self.BookFoundCheck = catalog.SearchLoanBookKey(self,self.OptionlistLoan[Choice-1])
                    if self.BookFoundCheck == True:
                        print("Loaned book was found")
                        break
                elif (Choice == 5):
                    break
                if (self.BookFoundCheck == False):
                    print("loaned Book wasn't found")
                    break
            else:
                print("Please enter a valid number")
                OneRunCheck = True
        input("Press anykey to return: ")

    def SearchLoanBookKey(self,SearchKey):
        with open ("LoanAdministration.json") as getdata:
            data = json.load(getdata)
            if SearchKey == "alles":
                for book in data["loanItems"]:
                    if(self.SearchTerm in book["title"] or self.SearchTerm in book["ISBN"] or self.SearchTerm in book["author"] or self.SearchTerm in book["Username"]):
                        self.BookFoundCheck = True
                        print("Name Subscriber " + book["Username"] + " || "+ "Title: " + book["title"] + " || Author: " + book["author"] +  " || ISBN: " + book["ISBN"])
            else:
                for book in data["loanItems"]:
                    if(self.SearchTerm in book[SearchKey]):
                        self.BookFoundCheck = True
                        print("Name Subscriber " + book["Username"] + " || "+ "Title: " + book["title"] + " || Author: " + book["author"] +  " || ISBN: " + book["ISBN"])
            return self.BookFoundCheck