# Generated by Django 3.0.5 on 2020-04-28 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('imageupload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadedimage',
            name='image_file',
            field=models.FileField(upload_to='static/searched-images/'),
        ),
    ]
