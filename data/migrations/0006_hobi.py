# Generated by Django 3.1.2 on 2021-04-21 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0005_wilayah_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hobi',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobi', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Hobi',
            },
        ),
    ]
