# Generated by Django 2.2.9 on 2020-02-04 20:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_blog_home'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='content',
            field=models.TextField(),
        ),
    ]
