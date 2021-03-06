# Generated by Django 2.2.5 on 2021-09-12 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0006_remove_signup_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='signup',
            name='image',
            field=models.FileField(blank=True, upload_to='courier.static.images'),
        ),
        migrations.AlterField(
            model_name='login',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
