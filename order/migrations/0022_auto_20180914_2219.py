# Generated by Django 2.0.6 on 2018-09-14 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0021_auto_20180914_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lineprofile',
            name='line_status_message',
            field=models.CharField(blank=True, max_length=1000, null=True, verbose_name='Line狀態訊息'),
        ),
    ]
