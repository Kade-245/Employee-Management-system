# Generated by Django 3.2.5 on 2022-03-02 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_information', '0004_employees_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='employees',
            name='dob',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='employees',
            name='gender',
            field=models.TextField(blank=True, null=True),
        ),
    ]
