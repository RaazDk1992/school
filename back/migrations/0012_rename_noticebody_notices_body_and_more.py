# Generated by Django 5.1.6 on 2025-03-25 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0011_alter_dynamic_files_alter_dynamic_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='notices',
            old_name='noticeBody',
            new_name='body',
        ),
        migrations.RenameField(
            model_name='notices',
            old_name='noticeTitle',
            new_name='title',
        ),
    ]
