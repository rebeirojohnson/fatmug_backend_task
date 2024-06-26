# Generated by Django 4.1.7 on 2024-05-01 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_remove_purchaseorder_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='address',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='average_response_time',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='contact_details',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='fulfillment_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='on_time_delivery_rate',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='vendor',
            name='quality_rating_avg',
            field=models.FloatField(null=True),
        ),
    ]
