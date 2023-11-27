# Generated by Django 4.2.7 on 2023-11-27 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_category_alter_product_image_product_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='reviews',
            field=models.ManyToManyField(to='post.review'),
        ),
    ]