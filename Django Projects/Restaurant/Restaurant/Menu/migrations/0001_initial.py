# Generated by Django 4.1.6 on 2023-02-13 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('item_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_name', models.CharField(max_length=100)),
                ('item_price', models.IntegerField(default=0)),
                ('item_description', models.TextField(default='')),
            ],
        ),
    ]