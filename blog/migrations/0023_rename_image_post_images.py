# Generated by Django 4.1.7 on 2023-02-26 06:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0022_alter_post_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='image',
            new_name='images',
        ),
    ]
