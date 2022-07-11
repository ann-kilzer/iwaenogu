# Generated by Django 4.0.6 on 2022-07-11 11:52

import colorfield.fields
from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('colors', '0003_auto_20200725_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorFamily',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=50)),
                ('name_ja', models.CharField(max_length=50)),
                ('hex_color', colorfield.fields.ColorField(default='#ffffff', max_length=18)),
                ('order', models.IntegerField())
            ],
        ),
    ]
