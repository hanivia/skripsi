# Generated by Django 3.2 on 2021-07-01 03:36

import appsantri.models
from django.db import migrations, models
import django_enumfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('appsantri', '0033_auto_20210701_0932'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesan',
            name='pesan_balasan_diniyah',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pesan',
            name='pesan_balasan_lembaga',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pesan',
            name='pesan_balasan_wilayah',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='pesan',
            name='status_diniyah',
            field=django_enumfield.db.fields.EnumField(default=0, enum=appsantri.models.PesanStatus),
        ),
        migrations.AddField(
            model_name='pesan',
            name='status_lembaga',
            field=django_enumfield.db.fields.EnumField(default=0, enum=appsantri.models.PesanStatus),
        ),
        migrations.AddField(
            model_name='pesan',
            name='status_wilayah',
            field=django_enumfield.db.fields.EnumField(default=0, enum=appsantri.models.PesanStatus),
        ),
    ]
