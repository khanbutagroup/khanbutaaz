# Generated by Django 4.0.3 on 2022-03-04 08:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_contactus'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contactus',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
