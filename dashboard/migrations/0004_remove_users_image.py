# Generated by Django 2.1.7 on 2019-12-20 13:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0003_auto_20191220_1246'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='image',
        ),
    ]
