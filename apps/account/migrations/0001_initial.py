# Generated by Django 3.1.3 on 2020-11-30 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=50, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('church_name', models.CharField(max_length=250)),
                ('sub_name', models.CharField(max_length=250)),
                ('short_name', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=250)),
                ('branch_pastor', models.CharField(max_length=250)),
                ('logo', models.ImageField(upload_to=None)),
                ('color', models.CharField(max_length=50)),
            ],
        ),
    ]
