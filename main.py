class ContactList(list):

    def search(self, string):
        name_list = []
        for element in self:
            if string in element.name:
                name_list.append(element)
        return name_list

    def longest_name(self):
        try:
            longest = self[0].name
        except:
            return None
        else:
            for element in self:
                if len(element.name) > len(longest):
                    longest = element.name
            return longest


class Contact:

    all_contacts = ContactList()

    def __init__(self, name, email):
        self.name = name
        self.email = email
        Contact.all_contacts.append(self)

    @classmethod
    def reset_contacts(cls):
        cls.all_contacts = ContactList()


class Supplier(Contact):
    all_orders = {}

    def __init__(self, name, email):
        super().__init__(name, email)
        Supplier.all_orders[self.email] = []

    def order(self, string):
        Supplier.all_orders[self.email].append(string)
