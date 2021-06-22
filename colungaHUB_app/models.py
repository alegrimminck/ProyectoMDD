from django.db import models

# Create your models here.
class Organizacion(models.Model):
  name = models.CharField(max_length=255)
  description = models.CharField(max_length=255)
  fono = models.CharField(max_length=255)
  webpage_url = models.CharField(max_length=255, blank=True, null=True)
  facebook_url = models.CharField(max_length=255, blank=True, null=True)
  telegram_url = models.CharField(max_length=255, blank=True, null=True)
  instagram_url = models.CharField(max_length=255, blank=True, null=True)
  linkedin_url = models.CharField(max_length=255, blank=True, null=True)
  twitter_url = models.CharField(max_length=255, blank=True, null=True)
  flickr_url = models.CharField(max_length=255, blank=True, null=True)
  email = models.CharField(max_length=255)
  image = models.ImageField(blank=True, null=True)

  def __str__(self):
    return self.name