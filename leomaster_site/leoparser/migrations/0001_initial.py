# Generated by Django 2.0.6 on 2020-04-09 19:57

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion
import leoparser.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DocDelta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('delta', django.contrib.postgres.fields.jsonb.JSONField(default=list)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.TextField(unique=True)),
                ('content', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(leoparser.models.TrackChangeMixin, leoparser.models.TrackAddMixin, models.Model),
        ),
        migrations.CreateModel(
            name='RemovableHistoryDocument',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uid', models.TextField(unique=True)),
                ('content', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
            bases=(leoparser.models.TrackChangeMixin, leoparser.models.TrackAddMixin, leoparser.models.TrackRemoveMixin, models.Model),
        ),
        migrations.CreateModel(
            name='Rule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='name')),
                ('xpath', models.TextField(verbose_name='xpath')),
                ('regex', models.TextField(blank=True, verbose_name='regex')),
                ('sub', models.TextField(blank=True, verbose_name='sub')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='children', to='leoparser.Rule')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='TypeOf',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(choices=[('container', 'container'), ('currency', 'currency'), ('date', 'date'), ('datetime', 'datetime'), ('float', 'float'), ('integer', 'integer'), ('string', 'string'), ('time', 'time')], unique=True, verbose_name='name')),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='rule',
            name='typeof',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leoparser.TypeOf'),
        ),
        migrations.AddField(
            model_name='docdelta',
            name='base',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='leoparser.Document'),
        ),
        migrations.AlterUniqueTogether(
            name='rule',
            unique_together={('name', 'parent')},
        ),
    ]
