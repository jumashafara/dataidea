# Generated by Django 4.2.4 on 2023-08-28 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0007_course_url'),
    ]

    operations = [
        migrations.CreateModel(
            name='VideoLink',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('url', models.URLField()),
            ],
        ),
        migrations.AddField(
            model_name='course',
            name='video_links',
            field=models.ManyToManyField(default='No Videos', to='school.videolink'),
        ),
    ]
