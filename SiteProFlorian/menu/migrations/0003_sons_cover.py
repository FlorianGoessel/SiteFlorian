# Generated by Django 4.0.2 on 2022-03-02 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0002_sons_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='sons',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
