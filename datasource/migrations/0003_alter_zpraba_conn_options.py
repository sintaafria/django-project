# Generated by Django 4.2.2 on 2023-06-18 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('datasource', '0002_alter_zpraba_conn_desc'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='zpraba_conn',
            options={'ordering': ['conn_name']},
        ),
    ]
