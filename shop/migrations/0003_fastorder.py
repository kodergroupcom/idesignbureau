# Generated by Django 3.2 on 2022-04-25 00:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20220425_0330'),
    ]

    operations = [
        migrations.CreateModel(
            name='FastOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productcode', models.CharField(max_length=255)),
                ('product', models.CharField(blank=True, max_length=255, null=True)),
                ('telefon', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Sifarişlər',
                'verbose_name_plural': 'Sifarişlər',
            },
        ),
    ]
