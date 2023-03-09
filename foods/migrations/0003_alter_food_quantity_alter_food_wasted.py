# Generated by Django 4.1.3 on 2022-11-15 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('foods', '0002_alter_category_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='quantity',
            field=models.IntegerField(blank=True, default=1),
        ),
        migrations.AlterField(
            model_name='food',
            name='wasted',
            field=models.BooleanField(blank=True),
        ),
    ]