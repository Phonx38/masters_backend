# Generated by Django 3.2.6 on 2021-08-20 08:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GstInfo',
            fields=[
                ('gstin_id', models.CharField(max_length=15, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('addrs_line_1', models.CharField(blank=True, max_length=150, null=True)),
                ('addrs_line_2', models.CharField(blank=True, max_length=150, null=True)),
                ('addrs_line_3', models.CharField(blank=True, max_length=150, null=True)),
                ('pincode', models.CharField(blank=True, max_length=6, null=True, validators=[django.core.validators.RegexValidator('^\\d{1,6}$')])),
                ('registration_date', models.DateField(verbose_name='Date_registration')),
                ('cancellation_date', models.DateField(blank=True, null=True, verbose_name='Date_Cancellation')),
                ('state_jurisdiction', models.CharField(blank=True, max_length=100, null=True)),
                ('center_jurisdiction', models.CharField(blank=True, max_length=100, null=True)),
                ('status_type', models.CharField(choices=[('ACTIVE', 'Active'), ('INACTIVE', 'Inactive')], default='INACTIVE', max_length=50)),
                ('taxpayer_type', models.CharField(choices=[('REGULAR', 'Regular'), ('COMPANY', 'Company'), ('FIRM', 'Firm')], default='REGULAR', max_length=50)),
                ('bussiness_type', models.CharField(choices=[('PRIVATE LIMITED COMPANY', 'Private Limited Company'), ('SOLE PROPERITERSHIP', 'Sole Properitership'), ('LLC', 'Llc')], default='LLC', max_length=100)),
            ],
        ),
    ]
