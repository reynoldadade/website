from django.http import HttpResponse
from .models import Album  # connect to the database
from django.template import loader


def index(request):  # request is any interaction with the web page
    all_albums = Album.objects.all()
    template = loader.get_template('')
    return HttpResponse('')


def detail(request, album_id):
    return HttpResponse("<h2> Details for album id: " + str(album_id) + "<h2>")
