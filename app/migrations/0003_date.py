# Generated by Django 2.0.6 on 2019-04-08 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_appointment_timeslot'),
    ]

    operations = [
        migrations.CreateModel(
            name='Date',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
            ],
        ),
    ]