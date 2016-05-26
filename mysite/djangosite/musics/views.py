from django.shortcuts import render,get_object_or_404

# Create your views here.
from django.http import Http404
from .models import Album,Song

def home(request):
	all_albums=Album.objects.all()
	context={'all_albums':all_albums}
	return render(request,'musics/home.html',context)

# def detail(request,album_id):

# 	try:
# 		album=Album.objects.get(pk=album_id)
# 	except Album.DoesNotExist:
# 		raise Http404('Album does not exist')
# 	return render(request,'musics/detail.html',{'album':album})


def detail(request,album_id):
	album=get_object_or_404( Album,pk=album_id)
	return render(request,'musics/detail.html',{'album':album})