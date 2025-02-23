# Generated by Django 4.2.4 on 2023-09-05 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0003_blogcomment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Hashnode',
        ),
        migrations.RenameField(
            model_name='blog',
            old_name='contentMarkdown',
            new_name='content_markdown',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='_id',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='coverImage',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='dateFeatured',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='dateUpdated',
        ),
        migrations.RemoveField(
            model_name='blogcomment',
            name='blog_slug',
        ),
        migrations.AddField(
            model_name='blog',
            name='cover_image',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='cuid',
            field=models.CharField(default='New Cuid', max_length=122),
        ),
        migrations.AddField(
            model_name='blog',
            name='date_featured',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='popularity',
            field=models.FloatField(default=0),
        ),
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.CharField(default='New Blog Slug', max_length=122),
        ),
        migrations.AddField(
            model_name='blogcomment',
            name='blog',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='blog.blog'),
        ),
        migrations.AlterField(
            model_name='blogcomment',
            name='user',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
