# Generated by Django 4.1 on 2023-04-10 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('audio_file', models.FileField(upload_to='audio/')),
                ('order', models.IntegerField(default=0)),
            ],
        ),
    ]
