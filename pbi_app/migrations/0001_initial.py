# Generated by Django 3.2.20 on 2023-09-01 07:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True, unique=True)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('content', models.TextField(null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.IntegerField(choices=[(0, 'Draft'), (1, 'Published')], default=0)),
                ('featured_image', models.ImageField(blank=True, default='placeholder_image', upload_to='images/')),
                ('likes', models.ManyToManyField(blank=True, related_name='blogpost_like', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, null=True)),
                ('website', models.CharField(max_length=50, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('external_link', models.URLField()),
                ('likes', models.ManyToManyField(blank=True, related_name='link_like', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=75, null=True, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('featured_image', models.ImageField(blank=True, default='placeholder_image', upload_to='images/')),
                ('likes', models.ManyToManyField(blank=True, related_name='gallery_like', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('body', models.TextField(max_length=80, null=True)),
                ('created_on', models.DateTimeField(auto_now_add=True, null=True)),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pbi_app.post')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
    ]
