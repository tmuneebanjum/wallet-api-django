# Generated by Django 3.2.4 on 2021-06-04 14:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userwallet', '0010_alter_user_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='email',
        ),
    ]
