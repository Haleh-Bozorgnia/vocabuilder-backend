# Generated by Django 4.2.5 on 2023-09-21 01:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Vocab',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vocab', models.CharField(max_length=200)),
                ('translation', models.CharField(max_length=200)),
                ('pronounciation', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
            ],
        ),
    ]
