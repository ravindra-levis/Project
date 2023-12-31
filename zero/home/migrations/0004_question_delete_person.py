# Generated by Django 4.1.2 on 2023-01-04 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_rename_name_person_username'),
    ]

    operations = [
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('pdf', models.FileField(upload_to='question/pdfs/')),
            ],
        ),
        migrations.DeleteModel(
            name='Person',
        ),
    ]
