# Generated by Django 2.2.9 on 2020-02-04 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_project_home'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='pdf',
            field=models.FileField(blank=True, upload_to='project_pdfs'),
        ),
    ]
