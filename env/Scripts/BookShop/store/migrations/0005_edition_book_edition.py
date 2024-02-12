# Generated by Django 5.0.1 on 2024-02-05 03:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_writer_firstname_alter_writer_bio_alter_writer_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='Edition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_ed', models.CharField(max_length=100)),
                ('add_ed', models.CharField(max_length=100)),
                ('code_ed', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='edition',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='store.edition'),
        ),
    ]
