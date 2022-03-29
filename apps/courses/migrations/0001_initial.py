# Generated by Django 4.0.1 on 2022-03-28 23:08

import apps.core.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', apps.core.models.UUIDPrimaryKeyField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('create_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', apps.core.models.UUIDPrimaryKeyField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', apps.core.models.UUIDPrimaryKeyField(editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('code', models.CharField(editable=False, max_length=10)),
                ('_class', models.CharField(choices=[('13', '13'), ('10', '10'), ('12', '12'), ('11', '11')], max_length=5)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='courses.course')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='subjects',
            field=models.ManyToManyField(to='courses.Subject'),
        ),
    ]
