# Generated by Django 2.2.2 on 2019-06-05 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='title',
            field=models.CharField(choices=[('ADM', 'Admin'), ('DOC', 'Doctor')], max_length=5),
        ),
    ]
