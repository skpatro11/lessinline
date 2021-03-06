# Generated by Django 3.2.7 on 2021-10-05 09:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business', '0003_auto_20211004_1933'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='staffs',
            field=models.ManyToManyField(blank=True, through='business.BusinessStaff', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='businessstaff',
            name='business',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='busisness_staffs', to='business.business'),
        ),
    ]
