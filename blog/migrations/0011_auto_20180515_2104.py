# Generated by Django 2.0.4 on 2018-05-15 12:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_auto_20180515_0753'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['-created_at'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Blogs'},
        ),
    ]