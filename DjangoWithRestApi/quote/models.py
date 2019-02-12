from django.db import models


class Quote(models.Model):
    quote = models.TextField()
    author = models.CharField(max_length=50)
    quote_date = models.DateField()
    email = models.EmailField(max_length=250)

    quote_category = models.ForeignKey(
        'QuoteCategory',
        on_delete=models.CASCADE
    )

    def __str__(self):
        if (len(self.quote) > 50):
            return self.quote[:50] + "..."
        else:
            return self.quote


class QuoteCategory(models.Model):
    category_name = models.CharField(max_length=100)

    def __str__(self):
        return self.category_name
