from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    publication_date = models.DateField()

def __str__(self):
    return self.title
