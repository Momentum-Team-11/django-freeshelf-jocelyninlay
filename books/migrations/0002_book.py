# Generated by Django 4.0.3 on 2022-03-07 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('author', models.CharField(max_length=225)),
                ('description', models.TextField()),
                ('url', models.CharField(max_length=750)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
