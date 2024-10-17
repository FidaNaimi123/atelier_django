# Generated by Django 4.2 on 2024-10-15 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='conference',
            name='start_date_before_end_date',
        ),
        migrations.AddConstraint(
            model_name='conference',
            constraint=models.CheckConstraint(check=models.Q(('start_date__lte', models.F('end_date'))), name='start_date_before_end_date'),
        ),
    ]
