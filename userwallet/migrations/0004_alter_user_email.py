# Generated by Django 3.2.4 on 2021-06-04 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userwallet', '0003_alter_user_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=1, max_length=32),
        ),
    ]
