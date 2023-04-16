POST /api/books

Request body:
{
  "book_name": "Harry Potter and the Philosopher's Stone",
  "author": "J.K. Rowling",
  "publisher": "Bloomsbury"
}

Response body:
{
  "id": 1,
  "book_name": "Harry Potter and the Philosopher's Stone",
  "author": "J.K. Rowling",
  "publisher": "Bloomsbury"
}
GET /api/books

Response body:
[
  {
    "id": 1,
    "book_name": "Harry Potter and the Philosopher's Stone",
    "author": "J.K. Rowling",
    "publisher": "Bloomsbury"
  },
  {
    "id": 2,
    "book_name": "The Lord of the Rings",
    "author": "J.R.R. Tolkien",
    "publisher": "Allen & Unwin"
  },
  {
    "id": 3,
    "book_name": "To Kill a Mockingbird",
    "author": "Harper Lee",
    "publisher": "J.B. Lippincott & Co."
  }
]
GET /api/books/{id}

Response body:
{
  "id": 1,
  "book_name": "Harry Potter and the Philosopher's Stone",
  "author": "J.K. Rowling",
  "publisher": "Bloomsbury"
}
PUT /api/books/{id}

Request body:
{
  "book_name": "Harry Potter and the Sorcerer's Stone",
  "author": "J.K. Rowling",
  "publisher": "Scholastic"
}

Response body:
{
  "id": 1,
  "book_name": "Harry Potter and the Sorcerer's Stone",
  "author": "J.K. Rowling",
  "publisher": "Scholastic"
}
DELETE /api/books/{id}

Response body:
{
  "message": "Book deleted successfully"
}
