from Books import books
import json

class loadAdministration():
    def __init__(self, LogInInfoLoan):
        self.__LogInInfoLoan = LogInInfoLoan
 
    def Inventory(self):
        checkInv = False
        with open ("LoanAdministration.json") as getdata:
            data = json.load(getdata)
        for loan in data['loanItems']:
            if(loan["Username"] == self.__LogInInfoLoan[0]):
                print("Title: " + loan["title"]  + " author: " + loan["author"] + " ISBN: " + loan['ISBN'])
                checkInv = True
        if(checkInv == False):
            print("you don't have any loaned books")
        input("press a key ")

    def formatting(self, Title):
        #clearscreen
        print(' \n'*20)
        print('\033[H\033[J', end='') 
        print("*" * 40)

        test = (40//2) - (len(Title) // 2) - 1
        if(len(Title) % 2 != 0):
            print("*" + (" " * int(test)) + Title + (" " * int(test-1))+ "*")
        else:
            print("*" + (" " * int(test)) + Title + (" " * int(test))+ "*")
        print("*" * 40)

    def showAllLoand_Books(self):
        boolcheck = False
        StopPoints =[15,30,45,60,75,90,105,120,135,140,145]
        try: 
            with open("LoanAdministration.json") as book:
                stuff_from_json = json.load(book)
                boolcheck = True
        except Exception:
            print("Their are no loaned books")
        counter = 0
        if boolcheck == True:
            for book in stuff_from_json["loanItems"]:
                print("Name Subscriber " + book["Username"] + " || "+ "Title: " + book["title"] + " || Author: " + book["author"] +  " || ISBN: " + book["ISBN"])
                counter += 1
                if(counter in StopPoints):
                    print("Enter x to return to Menu. Press any other key, to go to next page ")
                    a = input("enter: ")
                    if(a == "x"):
                        break
                    else:
                        loadAdministration.formatting(self, "All loaned books books")
            print("Total number of loaned books: " + str(counter))