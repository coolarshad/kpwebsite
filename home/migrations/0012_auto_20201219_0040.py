# Generated by Django 3.1.3 on 2020-12-18 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_aboutpage_aboutreview_clientreview'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutreview',
            name='review',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='clientreview',
            name='review',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='visionmission',
            name='mission',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='visionmission',
            name='vision',
            field=models.CharField(max_length=250),
        ),
    ]
