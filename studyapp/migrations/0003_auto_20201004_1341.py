# Generated by Django 3.0.5 on 2020-10-04 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0002_auto_20201004_1335'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='course_image',
            field=models.ImageField(default='', upload_to='images'),
        ),
    ]
