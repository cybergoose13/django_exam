# Generated by Django 2.2.4 on 2020-09-18 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam_project_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Like',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('liked_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='likes',
        ),
        migrations.AddField(
            model_name='wishes',
            name='likes',
            field=models.ManyToManyField(related_name='likes', to='exam_project_app.Like'),
        ),
    ]
