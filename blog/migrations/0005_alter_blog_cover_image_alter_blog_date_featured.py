# Generated by Django 4.2.4 on 2023-09-05 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_delete_hashnode_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='cover_image',
            field=models.CharField(default='', max_length=122),
        ),
        migrations.AlterField(
            model_name='blog',
            name='date_featured',
            field=models.CharField(default='', max_length=122),
        ),
    ]
