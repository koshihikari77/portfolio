# Generated by Django 2.0.4 on 2018-05-13 14:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blog_is_publick'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='pub_date',
        ),
    ]
