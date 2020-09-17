from django.db import models

# Create your models here.

class Artist(models.Model):
    name = models.CharField('Artist ame',max_length=200, unique=True)

    def __str__(self):
        return self.name

    # change model representation (useful in admin section)
    class Meta:
        verbose_name ='artist'


class Contact(models.Model):
    email = models.EmailField('Email',max_length=100)
    name = models.CharField('Name',max_length=200)

    def __str__(self):
        return self.name

    # change model representation (useful in admin section)
    class Meta:
        verbose_name ='client'

class Album(models.Model):
    reference = models.IntegerField('Album reference',null=True)
    created_at = models.DateTimeField('Creation date',auto_now_add=True)
    available = models.BooleanField('Is album avaible',default=True)
    title = models.CharField('Album title',max_length=200)
    picture = models.URLField('Image album (URL)',)
    artists = models.ManyToManyField(Artist, related_name='albums', blank=True)

    def __str__(self):
        return self.title
    
    # change model representation (useful in admin section)
    class Meta:
        verbose_name ='album'


class Booking(models.Model):
    created_at = models.DateTimeField('Reservation date',auto_now_add=True)
    contacted = models.BooleanField('Reservation  treated',default=False)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)
    album = models.OneToOneField(Album, on_delete = models.CASCADE)

    def __str__(self):
        return self.contact.name
    
    # change model representation (useful in admin section)
    class Meta:
        verbose_name ='reservation'

