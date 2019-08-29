# Generated by Django 2.2 on 2019-06-04 11:23

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_biodata', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currenteducation',
            name='semester',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]
