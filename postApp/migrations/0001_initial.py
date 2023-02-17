# Generated by Django 3.1 on 2023-02-16 04:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Title')),
                ('postDate', models.DateTimeField(default=datetime.datetime.now, verbose_name='Post published date and time')),
                ('image', models.CharField(blank=True, max_length=500, null=True, verbose_name='Image')),
                ('content', models.TextField(verbose_name='Content')),
            ],
        ),
    ]
