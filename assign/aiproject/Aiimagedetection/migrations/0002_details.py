# Generated by Django 3.1.7 on 2021-03-14 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Aiimagedetection', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('picname', models.CharField(max_length=350)),
                ('objectname', models.CharField(max_length=150)),
                ('xmin', models.IntegerField()),
                ('ymin', models.IntegerField()),
                ('xmax', models.IntegerField()),
                ('ymax', models.IntegerField()),
                ('timestamp', models.DateField(auto_now_add=True)),
            ],
        ),
    ]