# Generated by Django 3.2.7 on 2021-10-20 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='productscategory',
            name='is_active',
            field=models.BooleanField(db_index=True, default=True),
        ),
    ]