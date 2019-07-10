# Generated by Django 2.0.7 on 2018-07-25 17:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('bangla', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Most_read',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=500)),
                ('url', models.URLField()),
                ('time', models.DateTimeField(default=django.utils.timezone.now)),
                ('summary', models.CharField(max_length=2000)),
            ],
        ),
    ]
