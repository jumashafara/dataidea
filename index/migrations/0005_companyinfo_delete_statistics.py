# Generated by Django 4.2.4 on 2023-08-21 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0004_service_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompanyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='DataIdea', max_length=122)),
                ('highlight', models.CharField(default='Better Digital Experience With DataIdea', max_length=122)),
                ('description', models.TextField(default='We are a team of talented researchers and developers providing the best services by optimizing the latest tech')),
                ('clients', models.IntegerField(default=5)),
                ('projects', models.IntegerField(default=5)),
                ('workers', models.IntegerField(default=5)),
                ('hours_of_support', models.IntegerField(default=5)),
            ],
        ),
        migrations.DeleteModel(
            name='Statistics',
        ),
    ]
