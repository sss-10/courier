# Generated by Django 3.2.5 on 2021-09-10 03:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0003_auto_20210910_0907'),
    ]

    operations = [
        migrations.AlterField(
            model_name='signup',
            name='email',
            field=models.CharField(max_length=300, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='signup',
            name='user',
            field=models.CharField(max_length=200),
        ),
    ]
