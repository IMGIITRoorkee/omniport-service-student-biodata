# Generated by Django 2.1.3 on 2018-12-12 00:02

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import kernel.utils.upload_to


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.KERNEL_STUDENT_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('achievement', models.TextField()),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'swappable': 'STUDENT_BIODATA_ACHIEVEMENT_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=127)),
                ('year', models.IntegerField()),
                ('pages', models.CharField(blank=True, max_length=31)),
                ('volumes', models.CharField(blank=True, max_length=31)),
                ('contribution', models.CharField(blank=True, max_length=255)),
                ('editors', models.CharField(blank=True, max_length=255)),
                ('isbn_code', models.CharField(blank=True, max_length=255, verbose_name='ISBN code')),
                ('priority', models.IntegerField(default=0)),
                ('visibility', models.BooleanField(default=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'swappable': 'STUDENT_BIODATA_BOOK_MODEL',
            },
        ),
        migrations.CreateModel(
            name='CurrentEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('semester_number', models.IntegerField()),
                ('cgpa', models.DecimalField(decimal_places=3, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='CGPA')),
                ('sgpa', models.DecimalField(decimal_places=3, max_digits=5, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='SGPA')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'verbose_name_plural': 'current education',
                'swappable': 'STUDENT_BIODATA_CURRENTEDUCATION_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_full_date', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=127)),
                ('organisation', models.CharField(max_length=127)),
                ('description', models.TextField()),
                ('priority', models.IntegerField(default=0)),
                ('visibility', models.BooleanField(default=True)),
                ('experience_type', models.CharField(choices=[('job', 'Job'), ('int', 'Internship')], max_length=3)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'swappable': 'STUDENT_BIODATA_EXPERIENCE_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('topic', models.CharField(max_length=255)),
                ('priority', models.IntegerField(default=0)),
                ('visibility', models.BooleanField(default=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'swappable': 'STUDENT_BIODATA_INTEREST_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Paper',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('publisher', models.CharField(max_length=127)),
                ('year', models.IntegerField()),
                ('pages', models.CharField(blank=True, max_length=31)),
                ('volumes', models.CharField(blank=True, max_length=31)),
                ('journal', models.CharField(max_length=255)),
                ('priority', models.IntegerField(default=0)),
                ('visibility', models.BooleanField(default=True)),
                ('file', models.FileField(blank=True, null=True, upload_to=kernel.utils.upload_to.UploadTo('student_biodata', 'papers'))),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'swappable': 'STUDENT_BIODATA_PAPER_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_full_date', models.BooleanField(default=False)),
                ('position', models.CharField(max_length=127)),
                ('organisation', models.CharField(max_length=127)),
                ('description', models.TextField()),
                ('priority', models.IntegerField(default=0)),
                ('visibility', models.BooleanField(default=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'swappable': 'STUDENT_BIODATA_POSITION_MODEL',
            },
        ),
        migrations.CreateModel(
            name='PreviousEducation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('year', models.IntegerField()),
                ('institute', models.CharField(max_length=127)),
                ('field_of_study', models.CharField(blank=True, help_text='This can be a stream like Science or Commerce for school education', max_length=127)),
                ('degree', models.CharField(help_text='This can be a class like Class X or Class XII for school education', max_length=127)),
                ('graduation', models.CharField(choices=[('mat', 'Matriculate'), ('int', 'Intermediate'), ('ass', 'Associate'), ('gra', 'Graduate'), ('pos', 'Postgraduate'), ('doc', 'Doctorate'), ('pdo', 'Postdoctorate')], max_length=3)),
                ('priority', models.IntegerField(default=0)),
                ('visibility', models.BooleanField(default=True)),
                ('cgpa', models.DecimalField(blank=True, decimal_places=3, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(10.0)], verbose_name='CGPA')),
                ('percentage', models.DecimalField(blank=True, decimal_places=2, max_digits=5, null=True, validators=[django.core.validators.MinValueValidator(0.0), django.core.validators.MaxValueValidator(100.0)])),
                ('is_percentage', models.BooleanField(default=False)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'verbose_name_plural': 'previous education',
                'swappable': 'STUDENT_BIODATA_PREVIOUSEDUCATION_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('handle', models.SlugField(blank=True, max_length=31)),
                ('description', models.TextField()),
                ('custom_website', models.BooleanField(default=False)),
                ('resume', models.FileField(blank=True, null=True, upload_to=kernel.utils.upload_to.UploadTo('student_biodata', 'resume'))),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'swappable': 'STUDENT_BIODATA_PROFILE_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField(blank=True, null=True)),
                ('is_full_date', models.BooleanField(default=False)),
                ('priority', models.IntegerField(default=0)),
                ('visibility', models.BooleanField(default=True)),
                ('topic', models.CharField(max_length=127)),
                ('field', models.CharField(max_length=127)),
                ('description', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=kernel.utils.upload_to.UploadTo('student_biodata', 'projects'))),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'swappable': 'STUDENT_BIODATA_PROJECT_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Referee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=0)),
                ('visibility', models.BooleanField(default=True)),
                ('referee', models.CharField(max_length=255)),
                ('designation', models.CharField(max_length=127)),
                ('institute', models.CharField(max_length=255)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(max_length=255)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'swappable': 'STUDENT_BIODATA_REFEREE_MODEL',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_created', models.DateTimeField(auto_now_add=True)),
                ('datetime_modified', models.DateTimeField(auto_now=True)),
                ('priority', models.IntegerField(default=0)),
                ('visibility', models.BooleanField(default=True)),
                ('computer_languages', models.TextField(blank=True)),
                ('software_packages', models.TextField(blank=True)),
                ('additional_courses', models.TextField(blank=True)),
                ('minor_courses', models.TextField(blank=True)),
                ('languages', models.TextField(blank=True)),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.KERNEL_STUDENT_MODEL)),
            ],
            options={
                'swappable': 'STUDENT_BIODATA_SKILL_MODEL',
            },
        ),
    ]
