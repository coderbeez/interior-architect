# Generated by Django 2.2.9 on 2020-01-16 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_section_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='exclude',
            field=models.BooleanField(null=True),
        ),
    ]
