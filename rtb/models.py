from django.conf import settings
from django.db import models
from feedinator.models import Feed, FeedEntry
import gatekeeper

AFFILIATION_CHOICES = (
    ('d', 'Democrat'),
    ('i', 'Independent'),
    ('n', 'Non-partisan'),
    ('r', 'Republican'),
    ('x', 'Does not disclose'),
)

class Organization(models.Model):
    
    name = models.CharField(max_length=255)
    url = models.URLField(verify_exists=False)
    logo = models.URLField(verify_exists=False, blank=True, null=True)
    affiliation = models.CharField(max_length=1, choices=AFFILIATION_CHOICES)
    
    feed = models.OneToOneField(Feed)
    
    def __unicode__(self):
        return self.name

def mod(mo):
    entry = mo.content_object
    if not entry.feed.codename in ["press","rushedbills"]:
        content = entry.content.lower()
        for regex in settings.RTB_REGEX:
            if regex.search(content):
                return True
gatekeeper.register(FeedEntry, auto_moderator=mod)    
