# Generated by Django 3.2.5 on 2021-07-31 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_champion_api_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='description',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='card',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='card',
            name='talent',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='card',
            name='type',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='talent',
            name='description',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='talent',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='talent',
            name='type',
            field=models.CharField(max_length=30),
        ),
    ]
