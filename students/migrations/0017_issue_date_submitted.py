# Generated by Django 5.0.2 on 2024-04-11 17:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0016_issueadmin_user_delete_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='issue',
            name='date_submitted',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
