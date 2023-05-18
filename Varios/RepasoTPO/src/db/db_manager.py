import csv
from src.models.book import Book


def load_books():
    books = []
    with open('src/db/books.csv', 'r') as books_file:
        rows = csv.DictReader(books_file)

        for row in rows:
            books.append(
                Book(
                    row['ISBN'],
                    row['title'],
                    row['author'],
                    row['price'],
                    row['published'],
                    row['language'],
                    row['number_pages'],
                    row['press'],
                    row['ranking']
                )
            )

        return books


def save_purchase_order(purchase):
    with open('src/db/purchase_order.csv', 'a') as purchase_file:
        header = ['purchase_date', 'ISBN', 'user_id', 'full_address']

        writer = csv.DictWriter(purchase_file, fieldnames=header)

        if purchase_file.tell() == 0:
            writer.writeheader()

        writer.writerow(purchase)
