# Generated by Django 5.0.1 on 2024-02-07 13:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_alter_book_coverpage'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.edition'),
        ),
    ]