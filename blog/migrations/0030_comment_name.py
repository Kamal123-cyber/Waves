# Generated by Django 4.1.7 on 2023-03-04 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0029_remove_comment_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='name',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]