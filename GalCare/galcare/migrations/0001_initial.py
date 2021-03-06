# Generated by Django 3.2.6 on 2021-08-13 15:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=100)),
                ('quantity', models.PositiveSmallIntegerField(max_length=200, null=True)),
                ('design', models.CharField(max_length=100, null=True)),
                ('serial_number', models.CharField(max_length=50)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('seller', models.CharField(max_length=100)),
            ],
        ),
    ]
