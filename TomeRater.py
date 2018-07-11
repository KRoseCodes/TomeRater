class DuplicateUserEmail(Exception):
    pass

class InvalidUserEmail(Exception):
    pass

class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print ("""{}'s email has been updated.""".format(self.name))


    def __repr__(self):
        return """User {name}, email: {email}, books read: {books_n}""".format(name = self.name, email = self.email, books_n = len(self.books))

    def __eq__(self, other_user):
        return self.name == other_user.name and self.email == other_user.email

    def read_book(self, book, rating = None):
        self.books[book] = rating

    def get_average_rating(self):
        rating_accum = 0
        for value in self.books.values():
            if value != None:
                rating_accum += value
        return rating_accum / len(self.books)

class Book(object):
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.rating = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def change_isbn(self, new_isbn):
        self.isbn = new_isbn
        print ("""{}'s ISBN has been updated.""".format(self.title))

    def add_rating(self, rating):
        if rating >= 0 and rating <= 4:
            self.rating.append(rating)
        else:
            print("""Invalid Rating""")

    def __eq__(self, other_book):
        return self.title == other_book.title and self.isbn == other_book.isbn

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return author

    def __repr__(self):
        return """{title} by {author}""".format(title=self.title, author=self.author)

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def __repr__(self):
        return """{title}, a {level} manual on {subject}""".format(title=self.title, level=self.level, subject=self.subject)

class TomeRater(object):
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        book = Book(title, isbn)
        return book

    def create_novel(self, title, author, isbn):
        fiction = Fiction(title, author, isbn)
        return fiction

    def create_non_fiction(self, title, subject, level, isbn):
        non_fiction = Non_Fiction(title, subject, level, isbn)
        return non_fiction

    def add_book_to_user(self, book, email, rating = None):
        if not self.users[email]:
            print("""No user with email {email}!""".format(email=email))
        else:
            self.users[email].read_book(book, rating)
            book.add_rating(rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 1

    def add_user(self, name, email, books = None):
        try:
            user = User(name, email)
            self.users[email] = user
            if books != None:
                for book in books:
                    self.add_book_to_user(book, email)
        except DuplicateUserEmail:
            print ("ERROR: Account already exists with this email.")
        except InvalidUserEmail:
            print ("ERROR: Email does not exist.")

    def print_book_catalog(self):
        for book in self.books:
            if isinstance(book, Book):
                print(book)
            else:
                print("This is not a book.")

    def print_TomeRater_users(self):
        for email, user in self.users.items():
            if type(user) is User:
                print(user)
            else:
                print ("This is not a valid user.")

    def most_read_book(self):
        most_read_book = None
        num_of_reads = 0

        for book, reads in self.books.items():
            if reads > num_of_reads:
                num_of_reads = reads
                most_read_book = book
        return most_read_book

    def hightest_rating(self):
        hightest_num = 0
        hightest_rating = None

        for book in slef.books.keys():
            book_avg_num = book.get_average_rating()
            if book_avg_num > hightest_num:
                hightest_num = book_avg_num
                hightest_rating = book
        return hightest_rating




