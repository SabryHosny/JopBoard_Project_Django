# Generated by Django 3.1.5 on 2021-01-22 19:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jop_app', '0007_jop_applier_jop'),
    ]

    operations = [
        migrations.AddField(
            model_name='jop_applier',
            name='created_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]