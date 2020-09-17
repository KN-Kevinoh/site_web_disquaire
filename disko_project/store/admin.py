from django.contrib import admin
from .models import Album, Booking, Contact, Artist
from django.utils.safestring import mark_safe #interpreted html 
from django.urls import reverse # get page url from views name
from django.contrib.contenttypes.models import ContentType # get more infos from object as his belong model

# Register your models here to make it available to bakoffice
#admin.site.register(Booking)

class AdminURLMixin(object):
    
    def get_admin_url(self, obj):
        content_type = ContentType.objects.get_for_model(obj.__class__)
        return reverse('admin:store_%s_change' % (content_type.model), args=(obj.id,))

# class to display infos in multiline with columns
class BookingInline(admin.TabularInline, AdminURLMixin):
    # model to use 
    model = Booking
    # use one line 
    extra = 0
    #fieldsets = [(None, {'fields':['album_link', 'contacted']})]
    fields = ["created_at", "album_link", "contacted"]
    readonly_fields = ['created_at','album_link','contacted']
    # indicate fields to use 
    
    # change relations name
    verbose_name = "Reservation"
    verbose_name_plural = "Reservations"

    # avoid adding reservations manually
    def has_add_permission(self, request, obj = None):
        # make it return false
        return False
    
    def album_link(self, booking):
        url_detail_page = self.get_admin_url(booking.album)
        return mark_safe('<a href="{}">{}</a>'.format(url_detail_page,booking.album.title))

    


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

# album admin interface
@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    # specify search form fields
    search_fields = ['reference','title']

# booking admin interface
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin, AdminURLMixin):
    # restrict access to some fields for read only, and add link field as method (readonly execute items as method) instead of simple field
    readonly_fields = ['created_at','album_link','contact_link','contacted']
    fields = ["created_at", "contact_link", 'album_link', 'contacted']
    # set filter for research
    list_filter = ['created_at','contacted']

    # avoid adding reservations manually
    def has_add_permission(self, request):
        # make it return false
        return False
    
    def album_link(self, booking):
        url_detail_page = self.get_admin_url(booking.album)
        return mark_safe('<a href="{}">{}</a>'.format(url_detail_page,booking.album.title))

    def contact_link(self, booking):
        url_detail_page = self.get_admin_url(booking.contact)
        return mark_safe('<a href="{}">{}</a>'.format(url_detail_page,booking.contact.name))