# Generated by Django 4.1.5 on 2023-02-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Establishments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_est', models.CharField(max_length=100, verbose_name='название')),
                ('address', models.CharField(max_length=150, verbose_name='адрес')),
                ('price', models.IntegerField(verbose_name='ценовая категория')),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='имя')),
                ('surname', models.CharField(max_length=50, verbose_name='фамилия')),
                ('age', models.IntegerField(verbose_name='возраст')),
                ('gender', models.CharField(max_length=1, verbose_name='пол')),
                ('looking_gender', models.CharField(max_length=1, verbose_name='ищу_пол')),
            ],
        ),
    ]
