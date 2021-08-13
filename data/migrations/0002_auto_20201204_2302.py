# Generated by Django 3.0.8 on 2020-12-05 07:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jeniskelamin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jenis', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Jeniskelamin',
            },
        ),
        migrations.CreateModel(
            name='Lembaga',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Lembaga',
            },
        ),
        migrations.CreateModel(
            name='Tahunpelajaran',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tahun_pelajaran', models.CharField(max_length=200, null=True)),
            ],
            options={
                'verbose_name_plural': 'Tahunpelajaran',
            },
        ),
        migrations.AlterField(
            model_name='wilayah',
            name='nama',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
