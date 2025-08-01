# 1. Model the following
# a) A PhoneBook class that has a list of contacts
# The PhoneBook should support the following
# - ability to add contacts (check for phone number uniqueness)
# - ability to remove contacts
# - ability to check if a phone number is already in the contacts list
# - a display method that shows all contacts in a pretty way
# - implements the singleton design pattern
#
# b) 3 different types of contacts, Friend, Colleague, Relative, having the following attributes
#
# Friend:
# - name
# - phone number
# - favorite activity
# Colleague:
# - name
# - phone number
# - place of work
# Relative
# - name
# - phone number
# - type of relative (ex: mother, brother, etc.)
#
# The contacts should support the following:
# - equality comparison
# - string representation

from abc import ABC, abstractmethod

class Contact(ABC):
    def __init__(self, name: str, phone_number: str):
        self.name = name
        self.phone_number = phone_number

    def __eq__(self, other):
        return isinstance(other, Contact) and self.phone_number == other.phone_number

    @abstractmethod
    def __str__(self):
        pass


class Friend(Contact):
    def __init__(self, name: str, phone_number: str, favorite_activity: str):
        super().__init__(name, phone_number)
        self.favorite_activity = favorite_activity

    def __str__(self):
        return f"Friend: {self.name}, Phone number: {self.phone_number}, Likes: {self.favorite_activity}"


class Colleague(Contact):
    def __init__(self, name: str, phone_number: str, place_of_work: str):
        super().__init__(name, phone_number)
        self.place_of_work = place_of_work

    def __str__(self):
        return f"Colleague: {self.name}, Phone number: {self.phone_number}, Works: {self.place_of_work}"


class Relative(Contact):
    def __init__(self, name: str, phone_number: str, relation_type: str):
        super().__init__(name, phone_number)
        self.relation_type = relation_type

    def __str__(self):
        return f"Relative: {self.name}, Phone number: {self.phone_number}, Type of relative: {self.relation_type}"


# Singleton Design Pattern:
# Acest pattern asigură că o clasă are o singură instanță pe durata rulării programului
# și oferă un punct global de acces la ea. Este util atunci când vrem să controlăm accesul
# la o resursă comună (ex: agendă telefonică, conexiune la bază de date etc.).
# În Python, implementăm Singleton suprascriind metoda __new__ pentru a controla
# crearea obiectului și a returna mereu aceeași instanță.
class PhoneBook:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'contacts'):
            self.contacts = dict()

    def add_contact(self, contact: Contact) -> bool:
        if contact.phone_number not in self.contacts:
            self.contacts[contact.phone_number] = contact
            return True
        return False

    def remove_contact(self, phone_number: str) -> bool:
        return self.contacts.pop(phone_number, None) is not None

    def contains(self, phone_number: str) -> bool:
        return phone_number in self.contacts

    def display_contacts(self):
        if not self.contacts:
            print("PhoneBook is empty.")
        else:
            print("PhoneBook Contacts:")
            for contact in self.contacts.values():
                print(f" - {contact}")



if __name__ == "__main__":
    phonebook = PhoneBook()

    f1 = Friend("Alex", "123", "Football")
    c1 = Colleague("Maria", "456", "KFC")
    r1 = Relative("Bogdan", "789", "Brother")

    phonebook.add_contact(f1)
    phonebook.add_contact(c1)
    phonebook.add_contact(r1)

    phonebook.display_contacts()


    duplicate = Friend("Andrei", "123", "Driving")
    phonebook.add_contact(duplicate)


    phonebook.remove_contact("456")

    phonebook.remove_contact("789")

    phonebook.display_contacts()
