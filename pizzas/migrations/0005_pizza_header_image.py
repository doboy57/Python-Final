# Generated by Django 3.0.5 on 2021-12-12 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pizzas', '0004_pizza_owner'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='header_image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
