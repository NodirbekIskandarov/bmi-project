# Generated by Django 4.2.7 on 2023-12-08 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('order', '0002_orderinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderinfo',
            name='size',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='products.size'),
            preserve_default=False,
        ),
    ]
