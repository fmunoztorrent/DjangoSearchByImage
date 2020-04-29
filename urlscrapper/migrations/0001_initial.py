# Generated by Django 3.0.5 on 2020-04-28 01:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScrapedBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('link', models.TextField()),
                ('image_url', models.TextField()),
                ('procesed', models.BooleanField(default=False)),
                ('date_created', models.DateTimeField(default=django.utils.timezone.now)),
                ('catalog', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='catalogs.Catalog')),
            ],
        ),
    ]
