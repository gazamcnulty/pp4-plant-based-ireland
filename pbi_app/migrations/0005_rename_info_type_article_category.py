# Generated by Django 3.2.20 on 2023-09-01 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pbi_app', '0004_rename_info_type_news_article'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='info_type',
            new_name='category',
        ),
    ]