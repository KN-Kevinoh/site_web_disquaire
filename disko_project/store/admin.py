from django.contrib import admin
from .models import Album, Booking, Contact, Artist

# Register your models here to make it available to bakoffice
admin.site.register(Booking)

# class to display infos in multiline with columns
class BookingInline(admin.TabularInline):
    # model to use 
    model = Booking
    # indicate fields to use 
    fieldsets = [
        (None, {'fields':['album', 'contacted']})
    ]
    # use one line 
    extra = 0
    # change relations name
    verbose_name = "Reservation"
    verbose_name_plural = "Reservations"


class DiskArtistInline(admin.TabularInline):
    # use intermediate tables, because many to many relations
    model = Album.artists.through
    extra = 1
    # change relations name
    verbose_name = "Disk"
    verbose_name_plural = "Disks"


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    # display infos in multiline with columns
    inlines =[BookingInline, ]


# artists admin interface
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    # display infos in multiline with columns
    inlines =[DiskArtistInline, ]