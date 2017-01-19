# -*- coding: utf-8 -*-
# Generated by Django 1.9.12 on 2017-01-18 11:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndexedItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_type_pk', models.BigIntegerField(help_text='The primary key of the referenced content type.')),
                ('instance_pk', models.BigIntegerField(help_text='The primary key of the referenced instance.')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='The date on which this entry was created.')),
            ],
            options={
                'ordering': ('-created',),
            },
        ),
        migrations.AlterUniqueTogether(
            name='indexeditem',
            unique_together=set([('content_type_pk', 'instance_pk')]),
        ),
    ]
