# Generated by Django 3.0.4 on 2020-03-17 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0002_auto_20200317_1835'),
    ]

    operations = [
        migrations.CreateModel(
            name='shortURLManager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AddField(
            model_name='shorturl',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
