from flask import Flask
from flask import jsonify
from flask import request
from db.db_manager import load_books, save_purchase_order

app = Flask(__name__)
books = load_books()


@app.route('/api/academic-books/books', methods=['GET'])
def get_books():
    language_books = []

    language_param = request.args.get("language", "")
    if language_param == "EN" or language_param == "ES":
        for book in books:
            if book.language == language_param:
                language_books.append(book)
        return jsonify([book.serialize() for book in language_books])
    else:
        return jsonify([book.serialize() for book in books])


@app.route('/api/academic-books/books/<ISBN>', methods=['GET'])
def get_book_detail(ISBN):
    for book in books:
        if book.ISBN == ISBN:
            return jsonify(book.serialize_details())

    return jsonify(status=404, description="Book not found"), 404


@app.route('/api/academic-books/purchase-orders', methods=['POST'])
def create_purchase_order():
    if request.args['user_id'] == "univ_cema_9920":
        req_json = request.json
        save_purchase_order(req_json)

        return jsonify(req_json)

    else:
        return jsonify(status=404, description="User not found"), 404


if __name__ == '__main__':
    app.run()
