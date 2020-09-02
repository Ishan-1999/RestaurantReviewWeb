from django.db import models


# Create your models here.
class Review(models.Model):
    review_id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    ratings = models.CharField(max_length=10, default="5")
    review = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name


class Contact(models.Model):
    contact_id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    query = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name