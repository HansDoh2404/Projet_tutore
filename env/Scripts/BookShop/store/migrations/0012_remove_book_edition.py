# Generated by Django 5.0.1 on 2024-02-07 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_alter_book_edition'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='edition',
        ),
    ]
