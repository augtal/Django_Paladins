# Generated by Django 3.2.5 on 2021-07-31 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0003_role_long_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='damagetype',
            name='slug_name',
            field=models.CharField(default='aa', max_length=10),
            preserve_default=False,
        ),
    ]