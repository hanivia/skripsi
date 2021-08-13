# Generated by Django 3.1.2 on 2021-03-20 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_diniyah'),
        ('appsantri', '0008_auto_20210309_0314'),
    ]

    operations = [
        migrations.RenameField(
            model_name='santri',
            old_name='noi_jasah',
            new_name='no_ijasah',
        ),
        migrations.AddField(
            model_name='santri',
            name='diniyah',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='data.diniyah'),
        ),
    ]
