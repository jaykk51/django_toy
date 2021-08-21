# Generated by Django 3.1.1 on 2020-10-09 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Map',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='TITLE')),
                ('country', models.CharField(blank=True, max_length=100, verbose_name='COUNTRY')),
                ('url', models.URLField(unique=True, verbose_name='URL')),
            ],
        ),
    ]