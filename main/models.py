from django.db import models
from django.conf import settings
from django.contrib.sites.models import Site
import uuid

class Website(models.Model):
    # django site stuff
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1, editable=False)

    website_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=250)
    description = models.TextField(blank=True, default=None, null=True)
    url = models.CharField(max_length=250)

    def get_average_rating(self):
        # gets ratings based on average of ratings of all reviews
        # dummy value for now
        return 4

    def get_yellow_stars(self):
        return ['&#9733;' for i in range(0, self.get_average_rating())]

    def get_black_stars(self):
        return ['&#9733;' for i in range(0, 5-self.get_average_rating())]

    def __str__(self):
        return self.title

class Reviews(models.Model):
    # django site stuff
    site = models.ForeignKey(Site, on_delete=models.CASCADE, default=1, editable=False)

    review_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    website = models.ForeignKey("Website", on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    review = models.TextField(blank=True, default=None, null=True)
    calculated_rating = models.IntegerField()

    def get_yellow_stars(self):
        return ['&#9733;' for i in range(0, self.calculated_rating )]

    def get_black_stars(self):
        return ['&#9733;' for i in range(0, 5-self.calculated_rating )]

    def __str__(self):
        return str(self.website) + ' - ' + self.user.first_name + ' ' + self.user.last_name

