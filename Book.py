import json 
import collections
import random
class book():
    def __init__(self):
        self.BookISBN = ""
        self.Author = ""
        self.Country = ""
        self.ImageLink = ""
        self.Language = ""
        self.Link = ""
        self.Pages = 0
        self.Title = 0
        self.Year = 0
        self.Copies = 0
class books():
    def __init__(self):
        self.AllBooks = []
        self.AuthorCheck = ""
        self.TitleCheck = ""
        self.ISBN = ""
    def load_books(self):
        with open("Books.json", "r" , encoding="utf-8") as g:
            data = json.loads(g.read())
            for i in data:
                self.AllBooks.append(i)
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
    def Add_Book(self):
        temp = []
        try: 
            with open("Books.json") as f:
                for i in json.load(f):
                    temp.append(i)
        except Exception:
            pass
        Author = input("Please enter the Author's name: ")
        Country = input("Please enter the country from which the book originates: ")
        ImageLink = input("Please enter the file location of the BookCover: ")
        Language = input("Please enter the language of the book: ")
        link = input("Enter the URL of the wikipedia page of the book: ")
        Pages = int(input("Please enter the amount of pages the book has: "))
        Title = input("Please enter the Title of the book: ")
        Year = int(input("Please enter the year that the book was published: "))
        amountOfCopies = int(input("pleas enter amount of copies of this book: "))
        AddingBook = []
        isbn = books.CalculateISBN(self)
        AddingBook = { "author" : Author, "country" : Country, "imageLink" : ImageLink, "language" : Language, "link" :link, "pages" : Pages, "title" : Title, "year" : Year, "ISBN" : isbn, "Copies" : amountOfCopies }
        temp.append(AddingBook)
        #available
        #saved book
        with open("Books.json", "w", encoding="utf-8") as f:
            json.dump(temp, f, indent=4)
    def CalculateISBN(self):
        ISBN = ""
        for i in range(0, 9):
                ISBN += str(random.randrange(10))
                if i == 2 or i == 5:
                    ISBN += "-"
        return ISBN
    def rekendeel(self, lengtewoord):
        spaties = 50
        amountofSpaces =  spaties - len(lengtewoord)
        return amountofSpaces
    def showAll_books(self):
        boolcheck = False
        StopPoints =[15,30,45,60,75,90,105,120,135,140,145]
        try: 
            with open("Books.json") as book:
                stuff_from_json = json.load(book)
                boolcheck = True
        except Exception:
            print("Their are no books")
        counter = 0
        if boolcheck == True:
            for book in stuff_from_json:
                if(book["Copies"] >= 1):
                    print("Title: " + book["title"] + " || Author: " + book["author"] + " || Pages: " + str(book['pages']) + " || Year: " + str(book['year']) + " || ISBN: " + book['ISBN'] + " || Amount of copies: " + str(book["Copies"]))
                    counter += 1
                if(counter in StopPoints):
                    print("Enter x to return to Menu. Press any other key, to go to next page ")
                    a = input("enter: ")
                    if(a == "x"):
                        break
                    else:
                        books.formatting(self, "All avaible books")
            print("Total number of Copies books: " + str(counter))

    def check(self,author, ISBN, title):
        if(self.AuthorCheck == author and self.TitleCheck == title and self.ISBN == ISBN):
            return True
        else:
            return False
        
        