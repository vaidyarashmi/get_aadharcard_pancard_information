# Generated by Django 4.0 on 2022-01-10 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card_details', '0006_rename_aadhar_card_number_aadhar_card_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pan_card',
            name='number',
            field=models.IntegerField(),
        ),
    ]