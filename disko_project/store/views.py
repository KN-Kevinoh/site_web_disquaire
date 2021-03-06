from django.shortcuts import render, get_object_or_404
#from django.http import HttpResponse
from .models import Artist,  Album, Contact, Booking
#from django.template import loader # module loader to load templates
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .forms import ContactForm, FormatErrorList
from django.db import transaction, IntegrityError


# Create your views here.

def index(request):
    # get albums twolve first albums, in order by date creation 
    albums = Album.objects.filter(available=True).order_by('-created_at')[:12]
    #list_albums = ["<li>{}</li>".format(album.title) for album in albums]
    context = {'albums': albums}
    return render(request , 'store/index.html', context)


def listing(request):
    list_albums = Album.objects.filter(available=True)
    paginator = Paginator(list_albums, 9)
    # get page number
    page = request.GET.get('page')
    # send page number to paginator
    try:
        albums = paginator.page(page)
    except PageNotAnInteger:
        # page not an integer, deliver first page
        albums = paginator.page(1)
    except EmptyPage:
        # page out of bounds, deliver last page
        albums = paginator.page(paginator.num_pages)
    # set gabarit context
    context = {'albums': albums, 'paginate': True}
    return render(request, 'store/listing.html', context)



def details(request, id):
    album_id = int(id)
    #album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    artists_name = " ".join([artist.name for artist in album.artists.all()])
    # set gabarit context
    if album.picture and hasattr(album.picture, 'url'):
        image = album.picture.url
    else: 
        image = '#'
    context = {
        'album_title': album.title,
        'album_name': artists_name,
        'album_id': album.id,
        'thumbnail':  image
    }
    
    # check request type
    if request.method == "POST":
        # get form infos
        form = ContactForm(request.POST, error_class= FormatErrorList)
        if form.is_valid():
            """ is_valid method also convert the data to python object, 
             to use them, get them from django validation dictionnary """
            email = form.cleaned_data["email"]
            name = form.cleaned_data["name"]

            #email = request.POST.get("email")
            #name = request.POST.get("name")

            # run query try/except to avoid displaying error 500 when error occurred, just display simple error message
            try:
                # specify to treat all queries as transactions
                with transaction.atomic():
                    # get contact of email
                    contact = Contact.objects.filter(email=email)

                    if not contact.exists():
                        # create contact
                        contact = Contact.objects.create(email=email, name=name)
                    else:
                        # get contact from queryset, to make able the user can reserve more than one album
                        contact = Contact.first()
            
                    # get request album
                    album = get_object_or_404(Album, pk=album_id)
                    # create reservation
                    booking = Booking.objects.create(contact=contact, album=album)
                    # set available to false after booking
                    album.available = False
                    album.save()
                    # set context 
                    context = {'album_title': album.title}

                    return render(request, 'store/thanks.html', context)
            except IntegrityError:
                form.errors['internal'] = "Sorry! an error occurred, just trying again."
            
        else:
            context['form_errors'] = form.errors.items()
    else:
        form = ContactForm()
    context['form'] = form
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
