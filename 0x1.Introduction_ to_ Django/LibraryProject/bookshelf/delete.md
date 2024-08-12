from bookshelf.models import Book
book.delete()
books = Book.objects.all()
# output: <QuerySet []> 
