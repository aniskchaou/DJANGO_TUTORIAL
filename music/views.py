from django.shortcuts import render
from django.http import HttpResponse
from .models import Album
from django.template import loader
from django.http import Http404


def index(request):
   all_albums=Album.objects.all()
   html=''
   for album in all_albums:
   	   url='/music/'+str(album.id)+''
   	   html+='<a href="'+url+'">'+album.album_title+'</a><br>'
   #return render(request, "hello.html", {})
   return HttpResponse(html)

def viewArticle(request, articleId):
   text = "Displaying article Number : %s"%articleId
   return HttpResponse(text)

def detail(request,album_id):
	try:
		album=Album.objects.get(pk=album_id)
		context={'album':album}
	except Album.DoesNotExist:
		raise Http404("Album does not exist")
	return render(request,'detail.html',context)	
   	
def all(request):
	all_albums=Album.objects.all()
	template=loader.get_template('index.html')
	context={'all_albums':all_albums}
	return HttpResponse(template.render(context,request))   
