# Generated by Django 4.1.5 on 2023-02-12 19:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('acquaintance', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Establishments',
            new_name='Establishment',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
