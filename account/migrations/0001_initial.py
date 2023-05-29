# Generated by Django 4.2.1 on 2023-05-29 08:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('userid', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=50)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('role', models.CharField(choices=[('employer', 'Employer'), ('employee', 'Employee')], max_length=20)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'db_table': 'user',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employer',
            fields=[
                ('employerid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=200)),
                ('password', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=20)),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'verbose_name_plural': 'Employers',
                'db_table': 'employer',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('employeeid', models.AutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=100)),
                ('lastname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100)),
                ('phonenumber', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=50)),
                ('profession', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=20)),
                ('status', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.user')),
            ],
            options={
                'verbose_name_plural': 'Employees',
                'db_table': 'employee',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Certificate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('date_of_issuance', models.DateField()),
                ('certificate_file', models.FileField(upload_to='certificates/')),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.employee')),
            ],
            options={
                'verbose_name_plural': 'Certificates',
                'db_table': 'Certificate',
                'managed': True,
            },
        ),
    ]
