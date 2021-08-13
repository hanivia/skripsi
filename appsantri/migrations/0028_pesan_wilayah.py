# Generated by Django 3.2 on 2021-06-22 23:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0008_pendidikanayah_pendidikanibu_pendidikanwali_penghasilan'),
        ('appsantri', '0027_remove_pesan_wilayah'),
    ]

    operations = [
        migrations.AddField(
            model_name='pesan',
            name='wilayah',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.wilayah'),
        ),
    ]