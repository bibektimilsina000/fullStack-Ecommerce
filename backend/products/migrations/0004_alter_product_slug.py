# Generated by Django 4.1 on 2022-08-06 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0003_alter_product_thumbnail_alter_product_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="slug",
            field=models.SlugField(blank=True),
        ),
    ]
