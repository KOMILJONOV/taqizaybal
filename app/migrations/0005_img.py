# Generated by Django 4.0.6 on 2022-07-18 09:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_new_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Img',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='images/')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.new')),
            ],
        ),
    ]
