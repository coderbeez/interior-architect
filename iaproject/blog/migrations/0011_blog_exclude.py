# Generated by Django 2.2.9 on 2020-01-16 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_blog_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='exclude',
            field=models.BooleanField(null=True),
        ),
    ]