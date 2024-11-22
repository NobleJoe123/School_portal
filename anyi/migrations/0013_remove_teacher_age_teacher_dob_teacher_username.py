# Generated by Django 5.0.9 on 2024-11-22 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anyi', '0012_alter_student_department_art_commercial_jss1_jss2_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='age',
        ),
        migrations.AddField(
            model_name='teacher',
            name='dob',
            field=models.DateField(blank=True, null=True, verbose_name='Dob'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='username',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Username'),
        ),
    ]
