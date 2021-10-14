from django.db import models

# Create your models here.


class books(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(
        "LIBRARIAN.book_category",
        on_delete=models.CASCADE,
        null=True)
    publisher = models.ForeignKey(
        "LIBRARIAN.publishers",
        on_delete=models.CASCADE,
        null=True)
    author = models.ForeignKey(
        "LIBRARIAN.authors",
        on_delete=models.CASCADE,
        null=True)
    time_added = models.DateTimeField(auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name_plural = "Books"
        verbose_name = "Book"

    def __str__(self) -> str:
        return f'{self.id}'


class authors(models.Model):
    name = models.CharField(max_length=50)
    author_info = models.CharField(max_length=500, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Authors"
        verbose_name = "Author"

    def __str__(self) -> str:
        return f'{self.id}'


class publishers(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = "Publishers"
        verbose_name = "Publisher"

    def __str__(self) -> str:
        return f'{self.id}'


class book_category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Book Categories"
        verbose_name = "Book Category"

    def __str__(self):
        return self.name
