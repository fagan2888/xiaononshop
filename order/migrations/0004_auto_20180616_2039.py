# Generated by Django 2.0.6 on 2018-06-16 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0003_auto_20180616_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bento',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='dailymenu',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='order',
            name='create_time',
            field=models.DateTimeField(),
        ),
    ]
