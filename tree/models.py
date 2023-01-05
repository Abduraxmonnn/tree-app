from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Tree(models.Model):
    name = models.CharField(max_length=150)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.CharField(max_length=150)
    description = models.TextField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse(
            'item_detail',
            args=[str(self.name)]
        )
