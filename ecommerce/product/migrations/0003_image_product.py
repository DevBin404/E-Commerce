# Generated by Django 4.1.3 on 2022-11-03 13:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_image_rename_count_product_remaining_count_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.product'),
        ),
    ]
