# Generated by Django 2.2.16 on 2020-09-18 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20200918_0531'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='media/', verbose_name='Image album (URL)'),
        ),
    ]
