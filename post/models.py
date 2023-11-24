from django.db import models


# Create your models here.


class Product(models.Model):
    image = models.ImageField(upload_to= 'media/images/post', null=True, blank=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()
    created_ad = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.id} - {self.name}"


