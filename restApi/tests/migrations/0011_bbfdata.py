# Generated by Django 3.1.2 on 2020-10-10 10:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tests', '0010_kinawaydata'),
    ]

    operations = [
        migrations.CreateModel(
            name='BbfData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(blank=True, max_length=1000, null=True)),
                ('company_abn', models.CharField(max_length=100, unique=True)),
                ('summary', models.CharField(blank=True, max_length=4000, null=True)),
                ('products_services', models.CharField(blank=True, max_length=4000, null=True)),
            ],
        ),
    ]
