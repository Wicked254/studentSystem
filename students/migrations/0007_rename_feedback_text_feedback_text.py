# Generated by Django 5.0.2 on 2024-03-26 12:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_rename_text_feedback_feedback_text'),
    ]

    operations = [
        migrations.RenameField(
            model_name='feedback',
            old_name='feedback_text',
            new_name='text',
        ),
    ]
