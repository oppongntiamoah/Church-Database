# Generated by Django 3.1.4 on 2020-12-15 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0003_auto_20201213_1905'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='tithe',
            constraint=models.UniqueConstraint(fields=('member', 'month'), name='unique member month'),
        ),
    ]
