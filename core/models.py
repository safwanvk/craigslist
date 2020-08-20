from django.db import models


# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=120)
    created = models.DateTimeField(auto_created=True)
