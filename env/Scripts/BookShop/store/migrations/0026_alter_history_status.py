# Generated by Django 5.0.2 on 2024-02-08 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0025_alter_history_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='status',
            field=models.CharField(choices=[('En attente', 'En attente'), ('Accepté', 'Accepté'), ('Retourné', 'Retourné'), ('Refusé', 'Refusé')], default='En attente', max_length=100, null=True),
        ),
    ]