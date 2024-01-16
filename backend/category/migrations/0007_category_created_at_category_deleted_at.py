# Generated by Django 5.0.1 on 2024-01-16 04:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_category_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='created_at',
            field=models.DateTimeField(default=datetime.datetime(2024, 1, 16, 4, 33, 57, 440143)),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='category',
            name='deleted_at',
            field=models.DateTimeField(null=True),
        ),
    ]
