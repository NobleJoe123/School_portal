# Generated by Django 5.0.9 on 2024-11-18 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anyi', '0009_admin_image_bursal_image_teacher_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacher',
            name='date_joined',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='email',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='image',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='phonenum',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='username',
        ),
        migrations.AddField(
            model_name='teacher',
            name='address',
            field=models.TextField(blank=True, null=True, verbose_name='Address'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='Age'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='class_teacher',
            field=models.CharField(blank=True, choices=[('JSS1', 'JSS1'), ('JSS2', 'JSS2'), ('JSS3', 'JSS3'), ('SS1', 'SS1'), ('SS2', 'SS2'), ('SS3', 'SS3')], max_length=5, null=True, verbose_name='Class Teacher'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='cv',
            field=models.FileField(blank=True, null=True, upload_to='uploads/cv/', verbose_name='CV'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='emergency',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Emergency Contact'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='mname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Middle Name'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='passport',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/passport/', verbose_name='Passport Image'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Phone Number'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='sex',
            field=models.CharField(blank=True, choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6, null=True, verbose_name='Gender'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='subject_teacher',
            field=models.CharField(blank=True, choices=[('Mathematics', 'Mathematics'), ('English Language', 'English Language'), ('Nigerian Language', 'Nigerian Language'), ('Basic Science', 'Basic Science'), ('Social Studies', 'Social Studies'), ('Fine Arts/Creative Art', 'Fine Arts/Creative Art'), ('Agricultural Science', 'Agricultural Science'), ('Civic Education', 'Civic Education'), ('Christian Religion Studies', 'Christian Religion Studies'), ('Physical and Health Education', 'Physical and Health Education'), ('Business Studies', 'Business Studies'), ('French', 'French'), ('Computer Studies', 'Computer Studies'), ('Home Economics', 'Home Economics'), ('Basic Technology', 'Basic Technology'), ('Biology', 'Biology'), ('Physics', 'Physics'), ('Chemistry', 'Chemistry'), ('Further Mathematics', 'Further Mathematics'), ('Technical Drawing', 'Technical Drawing'), ('Food and Nutrition', 'Food and Nutrition'), ('Accounting', 'Accounting'), ('Commerce', 'Commerce'), ('Book-keeping', 'Book-keeping'), ('Data Processing', 'Data Processing'), ('Economics', 'Economics'), ('Government', 'Government'), ('Literature – in- English', 'Literature – in- English'), ('Christian Religion Knowledge', 'Christian Religion Knowledge'), ('Fine Art/Creative Art', 'Fine Art/Creative Art'), ('Geography', 'Geography')], max_length=50, null=True, verbose_name='Subject Teacher'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='fname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='First Name'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='password',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Password'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='sname',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Surname'),
        ),
    ]
