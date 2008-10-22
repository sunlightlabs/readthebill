from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render_to_response
from feedinator.models import FeedEntry
from readthebill.rtb.models import Organization
import gatekeeper

def index(request):
    entries = gatekeeper.approved(FeedEntry.objects.all())
    return render_to_response("index.html", {"entries": entries})

def partners(request):
    partners = Organization.objects.order_by('name')
    return render_to_response("partners.html", {"partners": partners})