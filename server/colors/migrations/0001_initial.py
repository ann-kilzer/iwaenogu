# Generated by Django 3.0.8 on 2020-07-24 06:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
        ('grains', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_en', models.CharField(max_length=50)),
                ('name_ja', models.CharField(max_length=50)),
                ('description_en', models.CharField(max_length=200)),
                ('hex_code', models.CharField(max_length=6)),
            ],
        ),
        migrations.CreateModel(
            name='Pigment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hex_code', models.CharField(max_length=6)),
                ('price', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='categories.Category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colors.Color')),
                ('grain', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='grains.Grain')),
            ],
        ),
    ]
