# Generated by Django 4.1.7 on 2023-02-26 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_rename_images_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='post_file/logo.png', null=True, upload_to='post_file'),
        ),
    ]