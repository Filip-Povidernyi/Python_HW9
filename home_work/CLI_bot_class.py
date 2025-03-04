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

    def edit_phone(self, old_phone: str, new_phone: str):

        for phone in self.phones:
            if phone.value == old_phone:
                phone.value = Phone(new_phone).value

                return f"Номер {old_phone} змінено на номер {new_phone}"

        raise ValueError(f"Номер {old_phone} не знайдено")

    def find_phone(self, f_phone: str):

        for phone in self.phones:
            if phone.value == f_phone:
                return phone

        return None


class AddressBook(UserDict):

    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def find(self, name: str):
        return self.data.get(name)

    def delete(self, name: str):

        if name in self.data:
            del self.data[name]


if __name__ == '__main__':
    book = AddressBook()

    # Створення запису для John
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Додавання запису John до адресної книги
    book.add_record(john_record)

    # Створення та додавання нового запису для Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Виведення всіх записів у книзі
    for name, record in book.data.items():
        print(record)

    # Знаходження та редагування телефону для John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  # Виведення: Contact name: John, phones: 1112223333; 5555555555

    # Пошук конкретного телефону у записі John
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  # Виведення: 5555555555

    # Видалення запису Jane
    book.delete("Jane")
