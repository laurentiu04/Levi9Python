'''
1. Model the following
a) A PhoneBook class that has a list of contacts
The PhoneBook should support the following
- ability to add contacts (check for phone number uniqueness)
- ability to remove contacts
- ability to check if a phone number is already in the contacts list
- a display method that shows all contacts in a pretty way

b) 3 different types of contacts, Friend, Colleague, Relative, having the following attributes

Friend:
- name
- phone number
- favorite activity
Colleague:
- name
- phone number
- place of work
Relative
- name
- phone number
- type of relative (ex: mother, brother, etc.)

The contacts should support the following:
- equality comparison
- string representation
'''

class Contact:
    def __init__(self, name:str, number:str):
        self.name = name
        self.number = number

    def __eq__(self, other):
        return self.name == other.name and self.number == other.number

class Friend(Contact):
    def __init__(self, name:str, number:str, activity:str):
        super().__init__(name, number)
        self.activity = activity

    def __str__(self):
        return f"|Name: {self.name}\t|Phone number: {self.number}\t|Favourite activity: {self.activity}"

class Colleague(Contact):
    def __init__(self, name:str, number:str, place:str):
        super().__init__(name, number)
        self.place = place

    def __str__(self):
        return f"|Name: {self.name}\t|Phone number: {self.number}\t|Work place: {self.place}"

class Relative(Contact):
    def __init__(self, name:str, number:str, relative_type:str):
        super().__init__(name, number)
        self.type = relative_type

    def __str__(self):
        return f"|Name: {self.name}\t|Phone number: {self.number}\t|Type: {self.type}"

class PhoneBook:
    def __init__(self):
        self.contacts = list()

    def add(self, contact:Contact):
        self.contacts.append(contact)
        self.contacts.sort(key=lambda e: e.name)

    def remove(self, contact):
        self.contacts.remove(contact)
    
    def exists(self, contact:Contact):
        if contact in self.contacts:
            return True
        
        return False

    def show_contants(self):
        print("\n========================| CONTACTS |========================")
        [print(c) for c in self.contacts]
        print("============================================================")


phonebook = PhoneBook()
friend = Friend("Yoshua", "0763541234", "Basketball")
rel = Relative("Ionut", "0766123743", "Uncle")
colegu = Colleague("Matei", "0739487562", "Simigerie")
phonebook.add(friend)
phonebook.add(rel)
phonebook.add(colegu)
phonebook.show_contants()
phonebook.remove(friend)
phonebook.show_contants()

