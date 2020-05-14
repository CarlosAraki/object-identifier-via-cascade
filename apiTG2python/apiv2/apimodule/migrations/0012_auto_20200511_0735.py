# Generated by Django 3.0.3 on 2020-05-11 10:35

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('apimodule', '0011_auto_20200510_2340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='picture_origin',
            name='uu_id',
            field=models.UUIDField(default=uuid.UUID('d9e8c3ec-4668-4242-8bba-5b313ba3f83a'), editable=False, unique=True),
        ),
    ]
