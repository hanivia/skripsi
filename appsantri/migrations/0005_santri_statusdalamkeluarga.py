# Generated by Django 3.0.8 on 2021-02-03 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appsantri', '0004_auto_20210125_2359'),
    ]

    operations = [
        migrations.AddField(
            model_name='santri',
            name='statusdalamkeluarga',
            field=models.CharField(blank=True, choices=[('Anak Kandung', 'Anak Kandung'), ('Anak Angkat', 'Anak Angkat'), ('Anak Asuh', 'Anak Asuh')], max_length=200, null=True),
        ),
    ]
