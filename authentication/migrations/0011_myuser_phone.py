# Generated by Django 3.0.8 on 2020-07-18 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0010_remove_myuser_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='phone',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]