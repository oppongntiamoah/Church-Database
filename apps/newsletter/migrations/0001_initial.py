# Generated by Django 3.1.4 on 2020-12-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Newsletter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('to', models.CharField(max_length=150)),
                ('msg', models.CharField(max_length=300)),
                ('via', models.CharField(max_length=5)),
                ('date_sent', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
