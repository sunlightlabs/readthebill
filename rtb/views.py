from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from feedinator.models import FeedEntry

def index(request):
    entries = FeedEntry.objects.all()
    return render_to_response("index.html", {"entries": entries})