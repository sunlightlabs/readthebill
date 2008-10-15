from django import template
from django.template.loader import render_to_string
from readthebill.rtb.models import Organization
import random

register = template.Library()

@register.simple_tag
def random_orgs(count):
    orgs = Organization.objects.filter(logo__isnull=False)
    orgs = random.sample(orgs, count)
    return render_to_string("rtb/random_orgs.html", {"orgs": orgs})