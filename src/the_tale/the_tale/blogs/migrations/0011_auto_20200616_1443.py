# Generated by Django 3.0.7 on 2020-06-16 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0010_auto_20191204_1948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tag',
            name='meta_type',
            field=models.IntegerField(blank=True, choices=[], default=None, null=True),
        ),
    ]
