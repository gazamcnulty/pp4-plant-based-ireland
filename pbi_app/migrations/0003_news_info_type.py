# Generated by Django 3.2.20 on 2023-09-01 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pbi_app', '0002_article'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='info_type',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='pbi_app.article'),
        ),
    ]