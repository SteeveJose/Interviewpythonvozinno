# Generated by Django 3.1 on 2020-10-10 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resumeapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetails',
            name='Password',
            field=models.CharField(default='exit', max_length=120),
            preserve_default=False,
        ),
    ]
