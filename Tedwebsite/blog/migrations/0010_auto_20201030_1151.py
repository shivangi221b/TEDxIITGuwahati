# Generated by Django 3.1.2 on 2020-10-30 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20201026_2032'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='photo',
            field=models.TextField(default='img/bg-img/18.jpg'),
        ),
    ]