from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class UserProfile(models.Model):
        user            = models.OneToOneField(User)
        first_name      = models.CharField(max_length=100, blank=True)
	last_name       = models.CharField(max_length=100, blank=True)
        # The additional attributes we wish to include.
        website = models.URLField(blank=True)
        picture = models.ImageField(upload_to='profile_images/', blank=True)

        def __unicode__(self):
                return self.user.username

class UserPhoto(models.Model):

    user_id = models.ForeignKey(User, related_name='photos')
    title = models.CharField(max_length=1000, null=True, blank=True)
    image = models.ImageField(upload_to='user_images/')

    def __unicode__(self):
        return self.title or 'noname'	
