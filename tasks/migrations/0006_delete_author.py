# Generated by Django 4.2 on 2023-04-26 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0005_remove_author_student_class_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Author',
        ),
    ]