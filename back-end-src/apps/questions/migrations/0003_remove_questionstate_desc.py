# Generated by Django 2.0 on 2017-12-10 18:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0002_auto_20171210_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='questionstate',
            name='desc',
        ),
    ]
