# Generated by Django 4.1.5 on 2023-02-16 13:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date',
            new_name='pub_date',
        ),
        migrations.AddField(
            model_name='blog',
            name='img',
            field=models.ImageField(default='the_def_img.jpg', upload_to='media/'),
        ),
        migrations.AddField(
            model_name='blog',
            name='like',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='blog',
            name='comment',
            field=models.TextField(blank=True, max_length=300),
        ),
        migrations.CreateModel(
            name='Commentator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('like', models.BooleanField(default=False)),
                ('commentary', models.TextField(default='')),
                ('person', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.blog')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
