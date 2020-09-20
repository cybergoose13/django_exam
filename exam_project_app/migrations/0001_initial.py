# Generated by Django 2.2.4 on 2020-09-18 21:32

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='likes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15)),
                ('last_name', models.CharField(max_length=15)),
                ('user_email', models.CharField(max_length=25)),
                ('user_birthday', models.DateTimeField(blank=True, null=True, verbose_name='release')),
                ('password', models.CharField(max_length=15)),
                ('confirm_password', models.CharField(max_length=15)),
                ('wishes_granted', models.IntegerField(default=0)),
                ('wishes_pending', models.IntegerField(default=0)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Wishes',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wish_name', models.CharField(max_length=64)),
                ('wish_desc', models.TextField(default='No description has been added.')),
                ('wish_granted', models.BooleanField(default=False)),
                ('granted_at', models.DateTimeField(default=datetime.datetime.now)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wishes', to='exam_project_app.Register')),
            ],
        ),
    ]
