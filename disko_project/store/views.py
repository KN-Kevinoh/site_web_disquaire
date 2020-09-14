from django.shortcuts import render
from django.http import HttpResponse
from .models import Artist,  Album, Contact, Booking
from django.template import loader # module loader to load templates

# Create your views here.

def index(request):
    # get albums twolve first albums, in order by date creation 
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    list_albums = ["<li>{}</li>".format(album.title) for album in albums]
    #message = """<ul>{}</ul>""".format("\n".join(list_albums))
    template = loader.get_template('strore/index.html')
    return HttpResponse(template.render(request = request))

def listing(request):
    albums = Album.objects.filter(available=True)
    list_albums = ["<li>{}</li>".format(album.title) for album in albums]
    message = """<ul>{}</ul>""".format("\n".join(list_albums))
    return HttpResponse(message)

def details(request, id):
    album_id = int(id)
    album = Album.objects.get(pk=album_id)
    artists = " ".join([artist.name for artist in album.artists.all()])
    message = "Album name is {}. It wrote by {}".format(album.title, artists)
    return HttpResponse(message) 

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
        if not albums.exists():
            message = "Empty albums"
    else:
        albums = Album.objects.filter(title__icontains=query)

        if not albums.exists():
            # get all albums by matching artists name with query
            albums = Album.objects.filter(artists__name__icontains=query)
        if not albums.exists():
             message = "No albums found"

        else:
            albums = ["<li>{}</li>".format(album.title) for album in albums]
            message = """
                    Search results:\n
                    <ul>
                        {}
                    </ul>
                """.format("<li>{}</li>".join(albums))

    
    return HttpResponse(message)
