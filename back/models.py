from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django_ckeditor_5.fields import CKEditor5Field



class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    firstName = models.CharField(max_length=100)
    lastName  = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
@receiver(post_save, sender=User)
def save_profile(sender,instance, **kwargs):
        instance.profile.save()


class Notices(models.Model):
    noticeTitle = models.CharField(max_length=200)
    noticeBody = CKEditor5Field(config_name='extends')
    document = models.CharField(max_length=200)
    def __str__(self):
        return self.noticeTitle

class Gallery(models.Model):
    galleryName = models.CharField(max_length=200)

    def __str__(self):
        return self.galleryName
class Image(models.Model):
    gallery = models.ForeignKey(Gallery,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')  

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ForeignKey(Image, on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Menu(models.Model):
    menuItem = models.CharField(max_length=200)
    is_expandable = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.menuItem
class SubMenu(models.Model):
    menuRef = models.ForeignKey(Menu,on_delete=models.CASCADE)
    submenu = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.submenu



