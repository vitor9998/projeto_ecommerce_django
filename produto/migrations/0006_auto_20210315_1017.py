# Generated by Django 3.1.7 on 2021-03-15 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('produto', '0005_auto_20210301_1434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing',
            field=models.FloatField(verbose_name='Preço'),
        ),
        migrations.AlterField(
            model_name='produto',
            name='preco_marketing_promocional',
            field=models.FloatField(default=0, verbose_name='Preço Promo.'),
        ),
    ]