from django.db import models

# Choices for book genre
BOOK_GENRE = [
    ('Biography', 'Biography'),
    ('Comics, Graphic Novels & Manga', 'Comics, Graphic Novels & Manga'),
    ('Fantasy', 'Fantasy'),
    ('Fiction & Literature', 'Fiction & Literature'),
    ('Horror', 'Horror'),
    ('Mystery', 'Mystery'),
    ('Non-fiction', 'Non-fiction'),
    ('Self-help', 'Self-help'),
    ('Science Fiction', 'Science Fiction'),
    ('Teen & Young Adult', 'Teen & Young Adult'),
]

# Choices for rating a book
BOOK_RATINGS = [
    ('1/5', '1/5'),
    ('2/5', '2/5'),
    ('3/5', '3/5'),
    ('4/5', '4/5'),
    ('5/5', '5/5'),
]

# Creates Add Book model
class AddBook(models.Model):
    book_title = models.CharField(max_length=100, null=False)
    book_author = models.CharField(max_length=100, null=False)
    book_genre = models.CharField(max_length=50, choices=BOOK_GENRE)
    book_rating = models.CharField(max_length=10, choices=BOOK_RATINGS)

    objects = models.Manager()

# Allows references to return book's title & author
    def __str__(self):
        return self.book_title + ' ' + self.book_author