# Generated by Django 3.1 on 2020-09-11 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0011_auto_20200909_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dailyfood',
            name='portion',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=4, verbose_name='portion'),
        ),
    ]
