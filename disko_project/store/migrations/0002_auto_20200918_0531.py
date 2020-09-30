# Generated by Django 3.1.1 on 2020-09-18 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'album'},
        ),
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'artist'},
        ),
        migrations.AlterModelOptions(
            name='booking',
            options={'verbose_name': 'reservation'},
        ),
        migrations.AlterModelOptions(
            name='contact',
            options={'verbose_name': 'client'},
        ),
        migrations.AlterField(
            model_name='album',
            name='available',
            field=models.BooleanField(default=True, verbose_name='Is album avaible'),
        ),
        migrations.AlterField(
            model_name='album',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Creation date'),
        ),
        migrations.AlterField(
            model_name='album',
            name='picture',
            field=models.FileField(blank=True, null=True, upload_to='media', verbose_name='Image album (URL)'),
        ),
        migrations.AlterField(
            model_name='album',
            name='reference',
            field=models.IntegerField(null=True, verbose_name='Album reference'),
        ),
        migrations.AlterField(
            model_name='album',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Album title'),
        ),
        migrations.AlterField(
            model_name='artist',
            name='name',
            field=models.CharField(max_length=200, unique=True, verbose_name='Artist ame'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='contacted',
            field=models.BooleanField(default=False, verbose_name='Reservation  treated'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Reservation date'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.EmailField(max_length=100, verbose_name='Email'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Name'),
        ),
    ]
