from django.db import models


# Create your models here.

class Review(models.Model):
    name = models.CharField(max_length=255)



class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Product(models.Model):
    image = models.ImageField(upload_to='media/images/post', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    reviews = models.ManyToManyField(Review)
    price = models.FloatField()
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"
