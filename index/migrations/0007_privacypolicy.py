# Generated by Django 4.2.4 on 2023-09-11 08:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0006_termofservice'),
    ]

    operations = [
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Privacy Policy', max_length=122)),
                ('description', models.TextField(default='By using the services provided by Data Idea ("the Company"), you agree to comply with and be bound by the following Privacy Policy ("Privacy Policy"). If you do not agree with these terms, please do not use our services.')),
            ],
        ),
    ]
