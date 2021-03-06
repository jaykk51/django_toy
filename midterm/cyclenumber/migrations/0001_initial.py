# Generated by Django 3.1.1 on 2020-10-07 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cyclenumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='NAME')),
                ('tel', models.CharField(max_length=50, verbose_name='MOBILE')),
                ('brand', models.CharField(blank=True, max_length=50, verbose_name='BRAND')),
                ('modelname', models.CharField(blank=True, max_length=50, verbose_name='MODEL NAME')),
                ('number', models.CharField(max_length=50, unique=True, verbose_name='CYCLE NUMBER')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DATE')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='MODIFY DATE')),
            ],
        ),
    ]
