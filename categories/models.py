# categories/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=100)

    #def __str__(self):
     #   return f"Category({self.name}, {self.image})"

class Meta:
    verbose_name_plural = "Categories"


class Product(models.Model):
    name = models.CharField(max_length=50, unique=True)
    image = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.PositiveIntegerField(null=True)


    def __str__(self):
        return f"Product({self.name}, {self.image}, {self.category})"
class Meta:
    verbose_name_plural = "Products"
