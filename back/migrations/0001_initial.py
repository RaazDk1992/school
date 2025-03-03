# Generated by Django 5.1.6 on 2025-03-03 07:07

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentTypes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contentType', models.CharField(max_length=200)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('menuItem', models.CharField(max_length=200)),
                ('is_expandable', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('galleryName', models.CharField(max_length=200)),
                ('contentType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.contenttypes')),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery_images/')),
                ('gallery', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.gallery')),
            ],
        ),
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.CharField(max_length=500)),
                ('contentType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.contenttypes')),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.image')),
            ],
        ),
        migrations.CreateModel(
            name='Notices',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noticeTitle', models.CharField(max_length=200)),
                ('document', models.CharField(max_length=200)),
                ('contentType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.contenttypes')),
            ],
        ),
        migrations.CreateModel(
            name='SubMenu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('submenu', models.CharField(max_length=100)),
                ('is_active', models.BooleanField(default=True)),
                ('menuRef', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='back.menu')),
            ],
        ),
    ]
