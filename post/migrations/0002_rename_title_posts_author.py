# Generated by Django 3.2.23 on 2023-11-04 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='title',
            new_name='author',
        ),
    ]