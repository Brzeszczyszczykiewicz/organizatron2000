# Generated by Django 3.0.3 on 2021-04-13 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appeal', '0004_archiveappeal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appeal',
            name='answer',
            field=models.TextField(blank=True, default=None, max_length=1500, null=True),
        ),
    ]
