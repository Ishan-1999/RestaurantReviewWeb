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


class Querie(models.Model):
    query_id = models.AutoField(primary_key=True)
    date = models.CharField(max_length=50, default="")
    name = models.CharField(max_length=50, default="")
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    query = models.CharField(max_length=1000, default="")

    def __str__(self):
        return self.name


class Dishe(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=50, default="")
    category = models.CharField(max_length=50, default="")
    dprice = models.IntegerField(default=0)

    def __str__(self):
        return self.dname


class TodaysSpecial(models.Model):
    dish_id = models.AutoField(primary_key=True)
    dname = models.CharField(max_length=50, default="")
    dprice = models.IntegerField(default=0)

    def __str__(self):
        return self.dname