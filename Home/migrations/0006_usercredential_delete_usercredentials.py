# Generated by Django 5.1.4 on 2024-12-06 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_remove_event_public_or_private_event_is_private_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserCredential',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
                ('confirm_password', models.CharField(max_length=128)),
            ],
        ),
        migrations.DeleteModel(
            name='UserCredentials',
        ),
    ]