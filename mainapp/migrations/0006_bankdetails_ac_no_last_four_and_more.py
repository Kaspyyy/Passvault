# Generated by Django 4.2.1 on 2023-05-29 15:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0005_rename_bankdetail_bankdetails'),
    ]

    operations = [
        migrations.AddField(
            model_name='bankdetails',
            name='ac_no_last_four',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='paymentcard',
            name='card_no_last_four',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]