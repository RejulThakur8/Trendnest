# Generated by Django 5.1.1 on 2024-11-08 12:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_cartitem_size'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cartitem',
            old_name='size',
            new_name='Size',
        ),
    ]