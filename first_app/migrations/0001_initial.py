# Generated by Django 4.1 on 2022-08-28 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('overview', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('content', models.TextField()),
                ('thumbnail', models.ImageField(upload_to='')),
                ('featured', models.BooleanField()),
            ],
        ),
    ]
