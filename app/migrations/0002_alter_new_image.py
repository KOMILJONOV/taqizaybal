# Generated by Django 4.0.6 on 2022-07-16 11:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='new',
            name='image',
            field=models.ImageField(upload_to='meida/images/'),
        ),
    ]