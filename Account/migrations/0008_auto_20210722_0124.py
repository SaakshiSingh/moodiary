# Generated by Django 3.0.3 on 2021-07-21 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0007_auto_20210720_2319'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='dateCreated',
            field=models.DateField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='diary',
            name='dateModified',
            field=models.DateField(auto_now=True),
        ),
    ]