# Generated by Django 4.2.4 on 2023-10-02 13:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_author_blogcategory_delete_authors'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='blog.author'),
        ),
    ]
