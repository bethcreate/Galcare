# Generated by Django 3.2.6 on 2021-08-13 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('galcare', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='uploads'),
        ),
    ]