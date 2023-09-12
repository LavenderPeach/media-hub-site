from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.TextField()
    director = models.CharField(max_length=100)
    genre = models.CharField(max_length = 50)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    review = models.TextField(blank = True, null=True)
    poster_url = models.URLField()
    trailer = models.URLField()

    def __str__(self):
        return self.title