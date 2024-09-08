from django.db import models

# Create your models here.
#    Model for the Author.
class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
#    Model for the book.
class Book(models.Model):
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
