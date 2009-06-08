from django.contrib import admin
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.generic import GenericRelation
from simplesurvey.models import AnswerSet
from uspolitics.politicians.models import Politician

ON_BILL_CHOICES = (
    ('U', 'Unknown'),
    ('C', 'Cosponsor'),
    ('S', 'Supports'),
    ('O', 'Opposes'))

class LegislatorDetailManager(models.Manager):
    def get_query_set(self):
        return super(LegislatorDetailManager, self).get_query_set().extra(
            select={'num_calls': 'SELECT COUNT(*) FROM simplesurvey_answerset WHERE content_type_id=%s AND object_id=callingtool_legislatordetail.id'},
            select_params=(ContentType.objects.get(app_label='callingtool', model='legislatordetail').id,)
            )

class LegislatorDetail(models.Model):

    objects = LegislatorDetailManager()

    legislator = models.OneToOneField(Politician)

    on_bill = models.CharField(max_length=1, choices=ON_BILL_CHOICES, default='U')
    on_amendment = models.NullBooleanField(default=None)
    call_goal = models.SmallIntegerField(default=10)

    calls = GenericRelation(AnswerSet)

    def __unicode__(self):
        return u' '.join([self.legislator.get_title_display(), 
                          self.good_fname(), self.legislator.lastname])

    def good_fname(self):
        return self.legislator.nickname or self.legislator.firstname

    def is_cosponsor(self):
        return self.on_bill == 'C'

    def supports_bill(self):
        if self.on_bill in ('C','S'):
            return True
        elif self.on_bill == 'O':
            return False
        else:
            return None

    def he_or_she(self):
        if self.legislator.gender == 'F':
            return 'she'
        else:
            return 'he'

    def his_or_her(self):
        if self.legislator.gender == 'F':
            return 'her'
        else:
            return 'his'

    def him_or_her(self):
        if self.legislator.gender == 'F':
            return 'her'
        else:
            return 'him'

    def needs_more_calls(self):
        return self.calls.count() < self.call_goal

admin.site.register(LegislatorDetail)
