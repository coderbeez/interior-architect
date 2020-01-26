# Generated by Django 2.2.9 on 2020-01-26 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_example'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('Architecture', 'Architecture'), ('Interior Design', 'Interior Design'), ('Graphics', 'Graphics'), ('Other', 'Other')], default='Other', max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=200)),
                ('phone', models.CharField(blank=True, max_length=50)),
                ('location', models.CharField(blank=True, max_length=200)),
                ('query', models.TextField()),
                ('reply', models.TextField(blank=True)),
            ],
        ),
    ]
