# Generated by Django 4.2 on 2024-10-15 21:54

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('categories', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Conference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('start_date', models.DateField(default=datetime.date(2024, 10, 15))),
                ('end_date', models.DateField(default=datetime.date(2024, 10, 15))),
                ('location', models.CharField(max_length=255)),
                ('price', models.FloatField()),
                ('capacity', models.IntegerField(validators=[django.core.validators.MaxValueValidator(limit_value=900, message='capacity must be under 900')])),
                ('program', models.FileField(upload_to='files/', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['pdf', 'png', 'jpeg', 'jpg'], message='Seuls les fichiers PDF, PNG, JPEG et JPG sont autorisés.')])),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='conferences', to='categories.category')),
            ],
        ),
        migrations.AddConstraint(
            model_name='conference',
            constraint=models.CheckConstraint(check=models.Q(('start_date__gte', models.F('end_date'))), name='start_date_before_end_date'),
        ),
    ]
