from django.db import models


class Country(models.Model):
   name = models.CharField(max_length=50)

   def __str__(self):
      return self.name


class City(models.Model):
   name = models.CharField(max_length=50)
   country = models.ForeignKey(Country, on_delete=models.SET_NULL, null=True)

   def __str__(self):
      return f'{self.country.name} - {self.name}'


class Category(models.Model):
   name = models.CharField(max_length=100)

   def __str__(self):
      return self.name


class CategoryChild(models.Model):
   name = models.CharField(max_length=100)
   category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)

   def __str__(self):
      return f'{self.category.name} - {self.name}'
