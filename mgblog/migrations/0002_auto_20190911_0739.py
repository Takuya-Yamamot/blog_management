# Generated by Django 2.2.5 on 2019-09-11 07:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mgblog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plan',
            name='plan_overview',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mgblog.PlanOverView'),
        ),
    ]