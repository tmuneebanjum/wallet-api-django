# Generated by Django 3.2.4 on 2021-06-04 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userwallet', '0012_remove_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default=0, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.TextField(default=0, max_length=56),
        ),
    ]
