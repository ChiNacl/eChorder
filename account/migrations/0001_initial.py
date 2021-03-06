# Generated by Django 3.2.11 on 2022-01-20 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('email', models.CharField(max_length=60, unique=True, verbose_name='Email')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Date Joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='Last Login')),
                ('category', models.CharField(choices=[('CUSTOMER', 'Customer'), ('RESTAURANT MANAGER', 'Restaurant Manager'), ('***', '***')], default='CUSTOMER', max_length=18)),
                ('profile_image', models.ImageField(default='static/images/ques.jpeg', upload_to='image_uploads')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
