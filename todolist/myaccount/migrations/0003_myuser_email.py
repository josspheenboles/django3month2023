# Generated by Django 4.2.1 on 2023-05-28 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myaccount', '0002_remove_myuser_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='email',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
