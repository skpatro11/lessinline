# Generated by Django 3.2.7 on 2021-10-03 15:36

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='staffs',
            field=models.ManyToManyField(blank=True, through='business.BusinessStaff', to=settings.AUTH_USER_MODEL),
        ),
    ]
