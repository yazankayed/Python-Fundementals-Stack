# Generated by Django 2.2.4 on 2023-06-03 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_one', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='Nothing'),
        ),
    ]
