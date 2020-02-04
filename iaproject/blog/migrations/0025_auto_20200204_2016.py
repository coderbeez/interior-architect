# Generated by Django 2.2.9 on 2020-02-04 20:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20200204_2011'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='exclude',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='section',
            name='exclude',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='comment',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
