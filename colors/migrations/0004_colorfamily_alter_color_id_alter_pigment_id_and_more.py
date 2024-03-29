# Generated by Django 4.0.6 on 2022-07-11 16:31

import colorfield.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('colors', '0003_auto_20200725_1251'),
    ]

    operations = [
        migrations.CreateModel(
            name='ColorFamily',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=50)),
                ('name_ja', models.CharField(max_length=50)),
                ('hex_color', colorfield.fields.ColorField(default='#ffffff', max_length=18)),
                ('order', models.IntegerField()),
            ],
        ),
        migrations.AlterField(
            model_name='color',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='pigment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddField(
            model_name='color',
            name='color_family',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='colors.ColorFamily'),
        ),
    ]
