# Generated by Django 2.0.4 on 2018-04-22 01:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20180421_1708'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='put_date',
            new_name='pub_date',
        ),
    ]
