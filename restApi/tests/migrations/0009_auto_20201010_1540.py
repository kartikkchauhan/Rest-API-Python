# Generated by Django 3.1.2 on 2020-10-10 10:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0008_auto_20201010_1204'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='companydetails',
            name='company_email',
        ),
        migrations.RemoveField(
            model_name='companydetails',
            name='company_website',
        ),
    ]
