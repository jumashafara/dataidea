# Generated by Django 4.2.4 on 2023-08-19 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0003_rename_project_date_portfolio_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='description',
            field=models.TextField(default='One of our services'),
        ),
        migrations.AlterField(
            model_name='service',
            name='image',
            field=models.ImageField(default='services/service.html', upload_to='services'),
        ),
    ]
