from Accounts import Account
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
"""
    if numChoise < 1 or numChoise > 6:
        subMenu()

    if numChoise == 1:
        #booklistFunc
    elif numChoise == 2:
        #RequestBookFunc
    elif numChoise == 3:
        #InventoryFunc
    elif numChoise == 4:
        #SearchBookFunc
    elif numChoise == 5:
        #returnBookFunc
    else numChoise == 6:
        #startfunc
"""

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
"""
    if numChoise < 1 or numChoise > 6:
        subMenu()

    if numChoise == 1:
        #booklistFunc

    elif numChoise == 2:
        #AddBookFunc

    elif numChoise == 3:
        #AddSubscriberFunc

    elif numChoise == 4:
        #ImportBookFunc

    elif numChoise == 5:
        #ImportSubscriberFunc

    elif numChoise == 6:
        #MakeBackupFunc

    elif numChoise == 7:
        #RestoreBackupFunc

    elif numChoise == 8:
        #LoanedBookListFunc

    elif numChoise == 9:
        #SearchLoanedBookFunc

    else numChoise == 10:
        #startfunc
"""
mainMenu()