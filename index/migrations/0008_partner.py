# Generated by Django 4.2.4 on 2023-09-20 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0007_privacypolicy'),
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Partner', max_length=122)),
                ('image', models.CharField(default='partner', max_length=122)),
                ('url', models.CharField(default='No url', max_length=100)),
            ],
        ),
    ]
