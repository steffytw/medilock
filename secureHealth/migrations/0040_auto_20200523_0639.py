# Generated by Django 3.0.6 on 2020-05-23 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureHealth', '0039_insurancecompanylogin'),
    ]

    operations = [
        migrations.CreateModel(
            name='applyinsurance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('email', models.CharField(max_length=30)),
                ('date_of_birth', models.DateField()),
                ('address', models.TextField()),
                ('gender', models.CharField(max_length=20)),
                ('country', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(max_length=20)),
                ('district', models.CharField(max_length=20)),
                ('pincode', models.IntegerField()),
                ('mobile_number', models.IntegerField()),
                ('status', models.CharField(default='new', max_length=20)),
                ('hospital_name', models.CharField(max_length=20)),
                ('company', models.CharField(max_length=20)),
                ('insurance_number', models.IntegerField()),
                ('company_code', models.CharField(max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='insurancecompanylogin',
            options={'verbose_name_plural': 'Insurance Company Login Details'},
        ),
    ]
