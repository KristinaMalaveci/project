# Generated by Django 5.0.1 on 2024-01-18 11:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nameApp', '0002_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_title', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='nameApp.category'),
        ),
    ]
