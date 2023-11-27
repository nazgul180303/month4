from django.contrib import admin

# Register your models here.


from post.models import Product, Category, Review

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Review)