# Generated by Django 4.0.3 on 2022-03-18 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0002_rename_super_types_supertype'),
        ('supers', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='supers',
            new_name='Super',
        ),
    ]