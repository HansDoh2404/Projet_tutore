# Generated by Django 5.0.2 on 2024-02-08 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0029_alter_history_updated'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='is_scanned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='book',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]