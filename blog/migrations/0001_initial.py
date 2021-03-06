# Generated by Django 2.0.4 on 2018-04-21 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('put_date', models.DateField()),
                ('body', models.CharField(max_length=10000)),
                ('image', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
