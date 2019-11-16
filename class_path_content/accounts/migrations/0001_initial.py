# Generated by Django 2.2.7 on 2019-11-16 05:02

import class_path_content.accounts.managers
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('registration_number', models.CharField(max_length=25, unique=True, verbose_name='registration number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('is_teacher', models.BooleanField(default=False, verbose_name='is teacher')),
                ('is_student', models.BooleanField(default=False, verbose_name='is student')),
            ],
            options={
                'db_table': 'users',
                'managed': False,
            },
            managers=[
                ('objects', class_path_content.accounts.managers.CustomUserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state', models.CharField(max_length=2, verbose_name='state')),
                ('city', models.CharField(max_length=100, verbose_name='city')),
                ('street', models.CharField(max_length=250, verbose_name='street')),
                ('neighborhood', models.CharField(max_length=100, verbose_name='neighborhood')),
                ('number', models.IntegerField(verbose_name='number')),
                ('postal_code', models.CharField(max_length=250, verbose_name='postal_code')),
                ('complement', models.CharField(blank=True, max_length=250, null=True, verbose_name='complement')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified_at')),
            ],
            options={
                'db_table': 'address',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='cpf')),
                ('full_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='full name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
            ],
            options={
                'db_table': 'admin',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified_at')),
            ],
            options={
                'db_table': 'class',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Institution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified_at')),
            ],
            options={
                'db_table': 'institution',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified_at')),
            ],
            options={
                'db_table': 'program',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='cpf')),
                ('full_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='full name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
            ],
            options={
                'db_table': 'student',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cpf', models.CharField(blank=True, default=None, max_length=100, null=True, verbose_name='cpf')),
                ('full_name', models.CharField(blank=True, max_length=250, null=True, verbose_name='full name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified at')),
            ],
            options={
                'db_table': 'teacher',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='description')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='modified_at')),
                ('class_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='accounts.Class')),
                ('program', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='accounts.Program')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='accounts.Teacher')),
            ],
            options={
                'db_table': 'course',
            },
        ),
    ]
