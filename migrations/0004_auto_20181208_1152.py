# Generated by Django 2.1.3 on 2018-12-08 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student_biodata', '0003_auto_20181208_1151'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reference',
            name='body',
            field=models.TextField(blank=True, help_text='This field contains body of the reference letter (OPTIONAL)'),
        ),
    ]
