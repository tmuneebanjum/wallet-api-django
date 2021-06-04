# Generated by Django 3.2.4 on 2021-06-04 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userwallet', '0005_auto_20210604_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='balance',
            field=models.IntegerField(default=0, max_length=265),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(default=0, max_length=32),
        ),
        migrations.AlterField(
            model_name='user',
            name='postalcode',
            field=models.CharField(default=0, max_length=15),
        ),
    ]
