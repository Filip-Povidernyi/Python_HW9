from collections import UserDict


class Field:

    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return str(self.value)


class Name(Field):
    pass


class Phone(Field):

    def __init__(self, value: str):

        if len(value) != 10 or not value.isdigit():
            raise ValueError(
                f"Телефонний номер {value} повинен містити рівно 10 цифр!")

        super().__init__(value)


class Record:

    def __init__(self, name: str):
        self.name = Name(name)
        self.phones = []

    def __str__(self):

        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

    def add_phone(self, phone: str):
        self.phones.append(Phone(phone))

    def remove_phone(self, rem_phone: str):

        self.phones = [
            phone for phone in self.phones if phone.value != rem_phone]

    def edit_phone(self, old_phone, new_phone):

        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = Phone(new_phone).value

                return f"Номер {old_phone} змінено на номер {new_phone}"

        raise ValueError(f"Номер {old_phone} не знайдено")

    def find_phone(self, f_phone):

        for phone in self.phones:
            if phone.value == f_phone:
                return phone

        return None


class AdressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name):
        if name in self.data:
            del self.data[name]
