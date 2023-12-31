# Generated by Django 4.2 on 2023-12-26 16:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0003_habilities_statistics_character_languages_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='habilities',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.habilities'),
        ),
        migrations.AddField(
            model_name='character',
            name='statistics',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='characters.statistics'),
        ),
    ]
