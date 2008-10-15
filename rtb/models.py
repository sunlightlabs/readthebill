from django.db import models

class Organization(models.Model):
    
    name = models.CharField(max_length=255)
    url = models.URLField(verify_exists=False)
    logo = models.URLField(verify_exists=False, blank=True, null=True)
    
    def __unicode__(self):
        return self.name