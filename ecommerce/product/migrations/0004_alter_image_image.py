# Generated by Django 4.1.3 on 2022-11-10 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_image_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(upload_to='Products'),
        ),
    ]
