# Generated by Django 5.0 on 2023-12-24 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.TextField(blank=True, null=True),
        ),
    ]
