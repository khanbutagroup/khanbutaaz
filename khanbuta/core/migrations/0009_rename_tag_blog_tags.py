# Generated by Django 4.0.3 on 2022-03-04 07:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_tag_blog'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='tag',
            new_name='tags',
        ),
    ]