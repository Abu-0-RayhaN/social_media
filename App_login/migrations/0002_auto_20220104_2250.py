# Generated by Django 3.2.8 on 2022-01-04 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_login', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='media/profile_pics'),
        ),
        migrations.DeleteModel(
            name='Follow',
        ),
    ]
