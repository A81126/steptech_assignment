# Generated by Django 4.2.3 on 2023-08-01 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_rename_data_user_data_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data_users',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]