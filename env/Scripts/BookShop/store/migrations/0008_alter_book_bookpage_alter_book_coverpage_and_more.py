# Generated by Django 5.0.1 on 2024-02-07 00:13

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_book_nb_page'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='bookpage',
            field=models.FileField(upload_to='bookpage/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='coverpage',
            field=models.FileField(upload_to='coverpage/'),
        ),
        migrations.AlterField(
            model_name='book',
            name='edition',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='store.edition'),
        ),
        migrations.AlterField(
            model_name='book',
            name='nb_page',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.IntegerField(),
        ),
    ]
