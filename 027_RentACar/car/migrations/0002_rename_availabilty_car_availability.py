# Generated by Django 4.2.2 on 2023-06-13 17:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='availabilty',
            new_name='availability',
        ),
    ]
