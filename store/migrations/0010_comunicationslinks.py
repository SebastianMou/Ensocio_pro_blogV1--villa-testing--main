# Generated by Django 3.2.6 on 2022-06-26 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20220623_0229'),
    ]

    operations = [
        migrations.CreateModel(
            name='ComunicationsLinks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facebook', models.URLField(max_length=255)),
                ('instagram', models.URLField(max_length=255)),
                ('whatsapp', models.URLField(max_length=255)),
                ('blog', models.URLField(max_length=255)),
            ],
        ),
    ]
