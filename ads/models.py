from django.db import models
import datetime

class Gender(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Country(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Users(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    age = models.IntegerField()

    def __str__(self):
        return self.fullname

class Ad(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/ads/')
    description = models.CharField(max_length=100)
    country_id = models.ForeignKey(Country, on_delete=models.CASCADE)
    age_rating = models.IntegerField()
    gender_rating = models.ForeignKey(Gender, on_delete=models.CASCADE)
    validity_date = models.DateField( default=datetime.date.today)

    def __str__(self):
        return self.title


