# Generated by Django 3.2.20 on 2023-08-24 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbi_app', '0015_delete_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='excerpt',
        ),
    ]