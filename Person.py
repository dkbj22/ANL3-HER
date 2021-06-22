class Person:
  def __init__(self, gender, name, surename, streetAddress, zipcode, city, phoneNumber, emailAddress, username, userRoll):
    self.gender = gender
    self.name = name
    self.surename = surename
    self.streetAddress = streetAddress
    self.zipcode = zipcode
    self.city = city
    self.phoneNumber = phoneNumber
    self.emailAddress = emailAddress
    self.username = username
    self.userRoll = userRoll

  def display(self):
    print("The gender of the user is " + self.gender)
    print("The name of the user is " + self.name)
    print("The surename of the user is " + self.surename)
    print("The street address of the user is " + self.streetAddress)
    print("The zipcode of the user is " + self.zipcode)
    print("The city of the user is " + self.city)
    print("The phone number of the user is " + self.phoneNumber)
    print("The e-mail of the user is " + self.emailAddress)
    print("The username of the user is " + self.username)
    print("The user roll of the user is " + self.userRoll)


x = Person("Female", "Nisa", "Tutucu", "Overblaak", "3011 MH", "Rotterdam", "+31 6 29081759", "info@nisatutucu.nl", "nisatutucu",  "Admin")
x.display()