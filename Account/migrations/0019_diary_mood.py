# Generated by Django 3.0.3 on 2021-07-26 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0018_auto_20210725_0128'),
    ]

    operations = [
        migrations.AddField(
            model_name='diary',
            name='mood',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
