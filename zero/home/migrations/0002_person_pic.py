# Generated by Django 4.1.2 on 2022-12-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='pic',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]