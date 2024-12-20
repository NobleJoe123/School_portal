# Generated by Django 5.0.9 on 2024-10-23 15:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anyi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('middlename', models.CharField(blank=True, max_length=100, null=True)),
                ('addnumber', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('country', models.CharField(max_length=100)),
                ('lga', models.CharField(max_length=100)),
                ('address', models.TextField()),
                ('dob', models.DateField()),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('guardian', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=255)),
                ('dropdown', models.CharField(choices=[('school1', 'School 1'), ('school2', 'School 2'), ('school3', 'School 3'), ('school4', 'School 4'), ('school5', 'School 5'), ('school6', 'School 6')], max_length=10)),
            ],
        ),
        migrations.DeleteModel(
            name='AdminProfile',
        ),
    ]
