# Generated by Django 3.0.3 on 2020-03-12 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secureHealth', '0028_auto_20200312_1002'),
    ]

    operations = [
        migrations.CreateModel(
            name='holidayData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holiday_name', models.CharField(max_length=20)),
                ('holiday_day', models.CharField(max_length=20)),
                ('holiday_date', models.DateField()),
            ],
            options={
                'verbose_name_plural': 'Holidays',
            },
        ),
    ]
