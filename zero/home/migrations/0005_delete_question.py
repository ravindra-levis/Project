# Generated by Django 4.1.2 on 2023-01-04 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_question_delete_person'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Question',
        ),
    ]
