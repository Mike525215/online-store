# Generated by Django 4.1.4 on 2022-12-25 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("projectApp", "0004_alter_items_description_favourites_cart"),
    ]

    operations = [
        migrations.AddField(
            model_name="items",
            name="count_item",
            field=models.IntegerField(default=1),
        ),
    ]