# Generated by Django 3.2.3 on 2021-06-22 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colungaHUB_app', '0003_auto_20210622_1718'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organizacion',
            name='facebook_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='telegram_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='organizacion',
            name='webpage_url',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]