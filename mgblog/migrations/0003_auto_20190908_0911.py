# Generated by Django 2.2.5 on 2019-09-08 09:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mgblog', '0002_planoverview_client'),
    ]

    operations = [
        migrations.AlterField(
            model_name='planoverview',
            name='client_name',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
