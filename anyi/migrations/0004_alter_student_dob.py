# Generated by Django 5.0.9 on 2024-10-23 15:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anyi', '0003_student_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='dob',
            field=models.DateField(default=datetime.date.today),
        ),
    ]