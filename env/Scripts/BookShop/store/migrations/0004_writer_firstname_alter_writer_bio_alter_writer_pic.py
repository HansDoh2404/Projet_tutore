# Generated by Django 5.0.1 on 2024-02-05 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_alter_book_bookpage_alter_book_coverpage_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='writer',
            name='firstname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='writer',
            name='pic',
            field=models.FileField(null=True, upload_to='writer/'),
        ),
    ]
