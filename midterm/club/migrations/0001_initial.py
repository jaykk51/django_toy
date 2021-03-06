# Generated by Django 3.1.1 on 2020-10-09 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='CLUB NAME')),
                ('city', models.CharField(max_length=50, verbose_name='CLUB CITY')),
                ('tel', models.CharField(blank=True, max_length=50, verbose_name='MOBILE')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('location', models.CharField(blank=True, max_length=50, verbose_name='MEETING PLACE')),
                ('riding_dt', models.DateTimeField(verbose_name='MEETING DATE')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DATE')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='MODIFY DATE')),
            ],
            options={
                'ordering': ('-riding_dt',),
            },
        ),
    ]
