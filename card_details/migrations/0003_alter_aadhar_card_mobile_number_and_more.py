# Generated by Django 4.0 on 2022-01-09 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_details', '0002_alter_aadhar_card_aadhar_card_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aadhar_card',
            name='mobile_number',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='pan_card',
            name='mobile_number',
            field=models.IntegerField(),
        ),
    ]