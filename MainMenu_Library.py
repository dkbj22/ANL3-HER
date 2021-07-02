from Accounts import Account
from Book import books
from LoanItem import LoanItem
from LoadAdministration import loadAdministration
from Catalog import catalog
from PublicLibrary import publicLibrary, Backup
from json import load

account = Account()
username = ""
bookclass = books()
publicLibraryclass = publicLibrary()
backupclass = Backup()
loadAdministrationclass = loadAdministration(username)
catalogclass = catalog()

def main():
    mainMenu()

def clear():
    print("\n"*100)

def Login():
    while True:
        global username
        username = [input("Enter your UserName: ")]
        logintype = account.Loginchecker(username)
        if logintype:
            return logintype
        else:
            print("Please enter valid information")

def mainMenu():
    global numChoise
    numChoise = 0
    startmenustatus = True
    logintype = ""

    while startmenustatus == True:

        clear()
        print("############################")
        print("                            ")
        print("        --Welcome--         ")
        print("                            ")
        print("1. Login                   ~")
        print("2. Register                ~")
        print("3. Quit                    ~")
        print("                            ")
        print("############################")
        choise = input("Make your choice: ")
        print("############################")

        try:
            numChoise = int(choise)
        except:
            mainMenu()
        
        if numChoise == 1:
            logintype = Login()
            print(logintype)
            if logintype == "Subscriber":
                subMenu()
            elif logintype == "Librarian":
                librMenu()
            startmenustatus = False
        elif numChoise == 2:
            account.Register("Subscriber")
            startmenustatus = False
            subMenu()
        elif numChoise == 3:
            startmenustatus = False
            exit()
        else:
            startmenustatus = True
            print("Invalid")

def subMenu():
    global numChoise
    global username
    numChoise = 0
    subscribermenustatus = True

    while subscribermenustatus == True:

        clear()
        print("############################")
        print("                            ")
        print("   --Welcome Subscriber--   ")
        print("                            ")
        print("1. Book List               ~")
        print("2. Request Book            ~")
        print("3. Inventory               ~")
        print("4. Search Book             ~")
        print("5. Return Book             ~")
        print("6. Logout                  ~")
        print("                            ")
        print("############################")
        choise = input("Make your choise: ")
        print("############################")

        try:
            numChoise = int(choise)
        except:
            subMenu()

        if numChoise < 1 or numChoise > 6:
            subMenu()
            subscribermenustatus = True
        if numChoise == 1:
            books.showAll_books()
            subscribermenustatus = True
        elif numChoise == 2:
            LoanItem(username).LoanItem()
            subscribermenustatus = True
        elif numChoise == 3:
            loadAdministration(username).Inventory()
            subscribermenustatus = True
        elif numChoise == 4:
            catalog.SearchBook()
            subscribermenustatus = True
        elif numChoise == 5:
            LoanItem(username).ReturnLoanedItem()
            subscribermenustatus = True
        elif numChoise == 6:
            mainMenu()
            subscribermenustatus = False


def librMenu():
    global numChoisse
    numChoise = 0
    librarymenustatus = True

    while librarymenustatus == True:
        clear()
        print("############################")
        print("                            ")
        print("     --Librarian Menu--     ")
        print("                            ")
        print("1. Book List               ~")
        print("2. Add Book                ~")
        print("3. Add Subscriber          ~")
        print("4. Import Book             ~")
        print("5. Import Subscriber       ~")
        print("6. Make Backup             ~")
        print("7. Restore Backup          ~")
        print("8. Loaned Book List        ~")
        print("9. Searched Loaned Book    ~")
        print("10. Logout                 ~")
        print("                            ")
        choise = input("Make your choice: ")
        print("                            ")
        print("############################")

        try:
            numChoise = int(choise)
        except:
            librMenu()

        if numChoise < 1 or numChoise > 10:
            librMenu()

        if numChoise == 1:
            bookclass.showAll_books()
            librarymenustatus = True

        elif numChoise == 2:
            bookclass.Add_Book()
            librarymenustatus = True
        elif numChoise == 3:
            account.Register("Subscriber")
            librarymenustatus = True
        elif numChoise == 4:
            publicLibraryclass.ImportBooks()
            librarymenustatus = True
        elif numChoise == 5:
            publicLibraryclass.ImportSubs()
            librarymenustatus = True
        elif numChoise == 6:
            backupclass.backups(1)
            librarymenustatus = True
        elif numChoise == 7:
            backupclass.backups(2)
            librarymenustatus = True
        elif numChoise == 8:
            loadAdministrationclass.showAllLoand_Books()
            librarymenustatus = True
        elif numChoise == 9:
            catalogclass.SearchLoanBook()
            librarymenustatus = True
        elif numChoise == 10:
            mainMenu()
            librarymenustatus = False

if __name__ == "__main__":
    main()