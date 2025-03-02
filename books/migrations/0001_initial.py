# Generated by Django 4.2 on 2025-02-27 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('author', models.CharField(max_length=100)),
                ('isbn', models.CharField(max_length=13, unique=True)),
                ('publication_date', models.DateField()),
                ('available_copies', models.IntegerField(default=1)),
            ],
        ),
    ]
