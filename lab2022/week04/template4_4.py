import datetime


class Document:
    def __init__(self, creation_date):
        pass

    def add_author(self, name):
        pass

    def __str__(self):
        pass


class Book(Document):
    def __init__(self, creation_date, title):
        pass

    def __str__(self):
        pass


class Email(Document):
    def __init__(self, creation_date, sender, subject):
        pass

    def add_recipient(self, name):
        pass

    def __str__(self):
        pass


if __name__ == "__main__":
    documents = []
    d1 = Document(datetime.datetime(2022, 3, 24, 9, 30))
    d1.add_author("Nikos")
    d2 = Document(datetime.datetime(2022, 3, 24, 10, 20))
    d2.add_author("Petros")
    d2.add_author("Maria")

    d3 = Book(datetime.datetime(2021, 1, 1, 0, 0), "Philosophy 101")
    d3.add_author("Socrates")
    d3.add_author("Descartes")
    d3.add_author("Nietschie")

    d4 = Email(datetime.datetime(2022, 3, 26, 10, 30), "Panayiotis", "Important notice")
    d4.add_author("Panayiotis")
    d4.add_recipient("Maria")

    d5 = Email(datetime.datetime(2022, 3, 21, 22, 45), "Marianthi", "SPAM")
    d5.add_author("Marianthi")
    d5.add_author("Vasilis")
    d5.add_recipient("Maria")
    d5.add_recipient("Christos")
    d5.add_recipient("Vasilis")
    d5.add_recipient("Sofia")

    documents.append(d1)
    documents.append(d2)
    documents.append(d3)
    documents.append(d4)
    documents.append(d5)

    for d in documents:
        print(d)
