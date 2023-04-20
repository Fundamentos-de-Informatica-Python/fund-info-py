class Book:

    def __init__(self, ISBN, title, author, price, published, langauge, number_pages, press, ranking) -> None:
        self.ISBN = ISBN
        self.title = title
        self.author = author
        self.price = price
        self.published = published
        self.language = langauge
        self.number_pages = number_pages
        self.press = press
        self.ranking = ranking

    def serialize(self):
        return {
            'ISBN': self.ISBN,
            'title': self.title,
            'author': self.author,
            'price': self.price
        }

    def serialize_details(self):
        return {
            'ISBN': self.ISBN,
            'title': self.title,
            'author': self.author,
            'price': self.price,
            'published': self.published,
            'language': self.language,
            'number_pages': self.number_pages,
            'press': self.press,
            'ranking': self.ranking
        }
