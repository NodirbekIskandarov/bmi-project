# Generated by Django 4.2.7 on 2023-12-08 06:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('New', 'New'), ('Completed', 'Completed')], default='New', max_length=10)),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.colors')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_info_product', to='products.product')),
                ('product_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='order_info_image', to='products.productimage')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_info_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
