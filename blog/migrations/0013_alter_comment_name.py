# Generated by Django 4.1.7 on 2023-02-22 15:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_alter_comment_options_remove_comment_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='name',
            field=models.OneToOneField(default=False, on_delete=django.db.models.deletion.CASCADE, related_name='name', to=settings.AUTH_USER_MODEL),
        ),
    ]
