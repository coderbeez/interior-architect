# Generated by Django 2.2.9 on 2020-02-06 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0025_auto_20200204_2016'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
