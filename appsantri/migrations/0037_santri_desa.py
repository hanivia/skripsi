# Generated by Django 3.2 on 2021-07-28 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsantri', '0036_auto_20210703_1917'),
    ]

    operations = [
        migrations.AddField(
            model_name='santri',
            name='desa',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
