from Accounts import Account
from Books import books
from LoanItem import LoanItem
from LoadAdministration import loadAdministration
from Catalog import catalog
from PublicLibrary import publicLibrary, Backup
from json import load

account = Account()

def clear():
    print("\n"*100)

def mainMenu():
    global numChoise
    numChoise = 0

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
    choise = input("Make your choise: ")
    print("############################")

    try:
        numChoise = int(choise)
    except:
        mainMenu()

    if numChoise == 1:
        account.Register("Subscriber")
    elif numChoise == 2:
        account.Register("Subscriber")
    elif numChoise == 3:
        exit()
    else:
        print("Invalid")

def subMenu():
    global numChoise
    numChoise = 0

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

    if numChoise == 1:
        books.showAll_books(self)
    elif numChoise == 2:
        LoanItem(self.__LogInInfo).LoanItem() #self.__logInfo is de username!, die moet nog gepakt worden!
    elif numChoise == 3:
        loadAdministration(self.__LogInInfo).Inventory()
    elif numChoise == 4:
        catalog.SearchBook()
    elif numChoise == 5:
        LoanItem(self.__LogInInfo).ReturnLoanedItem()
    else numChoise == 6:
        mainMenu()


def librMenu():
    global numChoisse
    numChoise = 0

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
    choise = input("Make your choise: ")
    print("                            ")
    print("############################")

    try:
        numChoise = int(choise)
    except:
        librMenu()

    if numChoise < 1 or numChoise > 10:
        librMenu()

    if numChoise < 1 or numChoise > 6:
        subMenu()

    if numChoise == 1:
        books.showAll_books(self)

    elif numChoise == 2:
        books.Add_Book(self)

    elif numChoise == 3:
        #AddSubscriberFunc MOET ALLE SOORTEN GEBRUIKERS KUNNEN TOEVOEGEN

    elif numChoise == 4:
        publicLibrary.ImportBooks()

    elif numChoise == 5:
        publicLibrary.ImportSubs()

    elif numChoise == 6:
        Backup.backups(1)

    elif numChoise == 7:
        Backup.backups(2)

    elif numChoise == 8:
        loadAdministration.showAllLoand_Books(self)

    elif numChoise == 9:
        catalog.SearchLoanBook()

    else numChoise == 10:
        mainMenu()