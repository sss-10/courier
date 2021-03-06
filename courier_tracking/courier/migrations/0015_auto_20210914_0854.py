# Generated by Django 2.2.5 on 2021-09-14 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courier', '0014_order_rstatus'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='raddress',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='rdate',
            new_name='date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='rid',
            new_name='mail',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='ridno',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='rmail',
            new_name='order',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='rname',
            new_name='phone',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='rorder',
            new_name='sid',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='rphone',
            new_name='sidno',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='rstatus',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='rweight',
            new_name='weight',
        ),
    ]
