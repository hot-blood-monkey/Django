# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
                ('image', models.ImageField(upload_to='images/%y/%m/%d')),
                ('description', models.DateField(db_index=True, auto_now_add=True)),
                ('user', models.ForeignKey(related_name='images_created', to=settings.AUTH_USER_MODEL)),
                ('user_like', models.ManyToManyField(blank=True, related_name='imaged_liked', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
