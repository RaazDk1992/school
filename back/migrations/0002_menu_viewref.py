# Generated by Django 5.1.6 on 2025-03-11 00:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('back', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='viewRef',
            field=models.CharField(default='back.views.dynamicView', max_length=100),
            preserve_default=False,
        ),
    ]
