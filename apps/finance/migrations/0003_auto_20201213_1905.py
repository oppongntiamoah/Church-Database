# Generated by Django 3.1.4 on 2020-12-13 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20201212_1617'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contribution',
            options={'verbose_name': 'contribution', 'verbose_name_plural': "contribution's"},
        ),
        migrations.RemoveField(
            model_name='contribution',
            name='visitor',
        ),
        migrations.RemoveField(
            model_name='giving',
            name='visitor',
        ),
        migrations.AlterField(
            model_name='donation',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
    ]
