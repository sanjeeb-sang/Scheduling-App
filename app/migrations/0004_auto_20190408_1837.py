# Generated by Django 2.0.6 on 2019-04-08 23:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_date'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Internship',
        ),
        migrations.DeleteModel(
            name='Job',
        ),
    ]