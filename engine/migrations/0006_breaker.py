# Generated by Django 3.1.7 on 2021-03-23 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engine', '0005_auto_20210322_2203'),
    ]

    operations = [
        migrations.CreateModel(
            name='breaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=50)),
                ('status', models.CharField(blank=True, max_length=10)),
                ('time', models.DateTimeField()),
            ],
            options={
                'db_table': 'breaker',
            },
        ),
    ]