# Generated by Django 2.1.3 on 2018-12-13 13:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Admin',
        ),
        migrations.RemoveField(
            model_name='city',
            name='state_name',
        ),
        migrations.RemoveField(
            model_name='locality',
            name='state_name',
        ),
        migrations.DeleteModel(
            name='SalesRegistration',
        ),
        migrations.DeleteModel(
            name='Suggestions',
        ),
        migrations.DeleteModel(
            name='Transaction',
        ),
        migrations.DeleteModel(
            name='UserRegistration',
        ),
        migrations.DeleteModel(
            name='City',
        ),
        migrations.DeleteModel(
            name='Locality',
        ),
        migrations.DeleteModel(
            name='State',
        ),
    ]
