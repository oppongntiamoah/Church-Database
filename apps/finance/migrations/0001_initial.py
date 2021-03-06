# Generated by Django 3.1.3 on 2020-11-30 11:37

from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('event', '0001_initial'),
        ('member', '0001_initial'),
        ('location', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, unique=True)),
                ('is_active', models.BooleanField(default=True)),
                ('start_date', models.DateField(blank=True)),
                ('end_date', models.DateField(blank=True)),
                ('note', models.TextField(blank=True)),
            ],
            options={
                'verbose_name': 'contribution Type',
                'verbose_name_plural': 'contribution Type',
            },
        ),
        migrations.CreateModel(
            name='Tithe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_received', models.DateField()),
                ('note', models.TextField(blank=True)),
                ('member', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='member.member')),
            ],
            options={
                'verbose_name': 'Tithe',
                'verbose_name_plural': 'Tithe',
            },
        ),
        migrations.CreateModel(
            name='Offertory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_received', models.DateField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='event.event')),
            ],
            options={
                'verbose_name': 'Offertory',
                'verbose_name_plural': 'Offertory',
            },
        ),
        migrations.CreateModel(
            name='Giving',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_received', models.DateField()),
                ('note', models.TextField(blank=True)),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='member.member')),
                ('visitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='member.visitor')),
            ],
            options={
                'verbose_name': 'Giving',
                'verbose_name_plural': 'Giving',
            },
        ),
        migrations.CreateModel(
            name='Donation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=20)),
                ('first_name', models.CharField(max_length=50)),
                ('middle_name', models.CharField(blank=True, max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_received', models.DateField()),
                ('occupation', models.CharField(blank=True, max_length=255)),
                ('workplace', models.CharField(blank=True, max_length=255)),
                ('school', models.CharField(blank=True, max_length=120)),
                ('note', models.TextField(blank=True)),
                ('address', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='location.address')),
            ],
            options={
                'verbose_name': 'Donation',
                'verbose_name_plural': "Donation's",
            },
        ),
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_received', models.DateField()),
                ('note', models.TextField(blank=True)),
                ('contribution_type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='finance.contribution_type')),
                ('member', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='member.member')),
                ('visitor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='member.visitor')),
            ],
            options={
                'verbose_name': 'contribution',
                'verbose_name_plural': "contribution's",
            },
        ),
    ]
