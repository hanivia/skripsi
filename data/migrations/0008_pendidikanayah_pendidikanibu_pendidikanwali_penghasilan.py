# Generated by Django 3.1.2 on 2021-04-21 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0007_agama_citacita_statusasalsantri_statushidupayah_statushidupibu'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pendidikanayah',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pendidikanayah', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pendidikanayah',
            },
        ),
        migrations.CreateModel(
            name='Pendidikanibu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pendidikanibu', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pendidikanibu',
            },
        ),
        migrations.CreateModel(
            name='Pendidikanwali',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pendidikanwali', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Pendidikanwali',
            },
        ),
        migrations.CreateModel(
            name='Penghasilan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('penghasilan', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Penghasilan',
            },
        ),
    ]
