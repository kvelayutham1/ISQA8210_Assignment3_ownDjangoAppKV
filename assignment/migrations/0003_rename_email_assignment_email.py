# Generated by Django 4.0.4 on 2022-04-16 07:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_assignment_email_alter_assignment_employee_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='assignment',
            old_name='Email',
            new_name='email',
        ),
    ]