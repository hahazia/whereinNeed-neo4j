from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.urls import reverse

class Charity(models.Model):
    name = models.CharField(max_length = 100)
    mission = models.TextField()
    webURL = models.URLField()
    ein = models.IntegerField()
    rating = models.IntegerField(null=True)
    category = models.ManyToManyField('Categ', blank = True)
    city = models.CharField(max_length = 20)
    zipCode = models.IntegerField(null = True)
    addr = models.CharField(max_length = 50)
    likes = models.ManyToManyField(User, related_name = 'likes', blank = True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return self.name

    def total_likes(self):
        return self.likes.count()


    def get_absolute_url(self):
        return reverse("charity_detail", args=[self.id])



class Categ(models.Model):
    name = models.CharField(max_length = 50)

    def __str__(self):
        return self.name




class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150,blank=True)
    bio = models.TextField()
    city = models.CharField(max_length=100, blank=True)
    date_joined = models.DateField(blank=True,null=True)


    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
