from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site

class Website(models.Model):
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1, editable=False)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, default=None, null=True)
    url = models.CharField(max_length=250)

class Reviews(models.Model):
    website = models.ForeignKey("Website", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    review = models.TextField(blank=True, default=None, null=True)

