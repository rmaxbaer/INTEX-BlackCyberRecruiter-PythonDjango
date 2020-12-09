# Generated by Django 3.1.4 on 2020-12-08 17:13


import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('applicant', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('company_name', models.CharField(max_length=50)),
                ('size', models.CharField(blank=True, max_length=4)),
                ('sectors', models.CharField(blank=True, max_length=4)),
                ('description', models.TextField(blank=True)),
                ('date_founded', models.DateField(blank=True, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=50)),
                ('address', models.CharField(blank=True, max_length=50)),
                ('city', models.CharField(blank=True, max_length=50)),
                ('state', models.CharField(blank=True, max_length=50)),
                ('zip', models.CharField(blank=True, max_length=50)),
                ('profile_picture', models.ImageField(blank=True, upload_to='profile_picture')),
                ('cover_picture', models.ImageField(blank=True, upload_to='cover_picture')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deadline', models.DateTimeField()),
                ('start_date', models.DateField()),
                ('message', models.TextField(blank=True)),
                ('compensation', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(default='extended', max_length=50)),
                ('offer_accepted', models.BooleanField(default=False)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applicant.application')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_title', models.CharField(max_length=50)),
                ('job_description', models.TextField()),
                ('contract_type', models.CharField(blank=True, max_length=50)),
                ('compensation', models.CharField(max_length=50)),
                ('relocation_assistance', models.BooleanField(default=False)),
                ('positions_available', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='organization.organization')),
                ('skills', models.ManyToManyField(blank=True, to='applicant.Skill')),
            ],
        ),
    ]
