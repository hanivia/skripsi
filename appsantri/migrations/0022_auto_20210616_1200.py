# Generated by Django 3.2 on 2021-06-16 05:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appsantri', '0021_auto_20210506_2009'),
    ]

    operations = [
        migrations.RenameField(
            model_name='santri',
            old_name='nis_lembaga',
            new_name='nis',
        ),
        migrations.RemoveField(
            model_name='santri',
            name='nis_pesantren',
        ),
    ]
