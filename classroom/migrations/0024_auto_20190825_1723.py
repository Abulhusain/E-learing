# Generated by Django 2.2.2 on 2019-08-25 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0023_remove_takenquiz_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myfile',
            name='file',
        ),
        migrations.AddField(
            model_name='myfile',
            name='file_link',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='course',
            name='code',
            field=models.CharField(max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='lesson',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
