# Generated by Django 4.1.4 on 2022-12-26 00:42

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projectApp", "0006_remove_items_count_item_cart_count_item"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="Favourites",
            new_name="Favorites",
        ),
    ]