# Generated by Django 5.0.6 on 2024-06-17 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadwaystudent',
            name='address',
            field=models.CharField(max_length=33, null=True),
        ),
        migrations.AlterField(
            model_name='broadwaystudent',
            name='name',
            field=models.CharField(help_text='student name', max_length=255, null=True),
        ),
    ]
