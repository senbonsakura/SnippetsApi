# Generated by Django 2.1.1 on 2018-09-24 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20180906_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='snippet',
            name='file',
            field=models.FileField(blank=True, null=True, upload_to='media'),
        ),
        migrations.AlterField(
            model_name='snippet',
            name='title',
            field=models.CharField(blank=True, default='Untitled', max_length=100),
        ),
    ]