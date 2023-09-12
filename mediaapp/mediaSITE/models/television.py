from django.db import models

class Television(models.Model):
    title = models.CharField(max_length=255)  # The movie's title
    release_date = models.DateField()  # The release date of the movie
    description = models.TextField()  # A description or summary of the movie
    creator = models.CharField(max_length=100)  # The director of the movie
    genre = models.CharField(max_length=50)  # The genre of the movie
    rating = models.DecimalField(max_digits=3, decimal_places=1)  # User rating (e.g., 4.5)
    review = models.TextField(blank=True, null=True)  # User review (optional)
    poster_url = models.URLField()  # URL to the movie's poster image
    trailer_url = models.URLField()  # URL to the movie's trailer

    def __str__(self):
        return self.title