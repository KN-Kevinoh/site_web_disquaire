from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Artist,  Album, Contact, Booking
#from django.template import loader # module loader to load templates


# Create your views here.

def index(request):
    # get albums twolve first albums, in order by date creation 
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    list_albums = ["<li>{}</li>".format(album.title) for album in albums]
    #message = """<ul>{}</ul>""".format("\n".join(list_albums))
    #template = loader.get_template('strore/index.html')
    # set gabarit context
    context = {'albums': albums}
    return render(request , 'store/index.html', context)


def listing(request):
    albums = Album.objects.filter(available=True)
    #list_albums = ["<li>{}</li>".format(album.title) for album in albums]
    #message = """<ul>{}</ul>""".format("\n".join(list_albums))
    context = {'albums': albums}
    return render(request, 'store/listing.html', context)

def details(request, id):
    album_id = int(id)
    #album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    artists_name = " ".join([artist.name for artist in album.artists.all()])
   
    context = {
        'album_title': album.title,
        'album_name': artists_name,
        'album_id': album.id,
        'thumbnail': album.picture
    }
    return render(request, 'store/details.html', context) 

def search(request):
    query = request.GET.get('query')
    if not query:
        albums = Album.objects.all()
        #if not albums.exists():
            #message = "Empty albums"
    else:
        albums = Album.objects.filter(title__icontains=query)

        if not albums.exists():
            # get all albums by matching artists name with query
            albums = Album.objects.filter(artists__name__icontains=query)
       # if not albums.exists():
           #  message = "No albums found"

      #  else:
          #  albums = ["<li>{}</li>".format(album.title) for album in albums]
          #  message = """
           #         Search results:\n
            #        <ul>
             #           {}
              #      </ul>
               # """.format("<li>{}</li>".join(albums))

    title = "Requests results of %s"%query

    context = {
        'albums': albums,
        'title':title
    }
    
    return render(request, 'store/search.html', context)
