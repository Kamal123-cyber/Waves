# Generated by Django 4.1.7 on 2023-04-28 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0002_payment_delete_order'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payment',
            new_name='Donations',
        ),
    ]
