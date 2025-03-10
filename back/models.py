from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.text import slugify
from django_ckeditor_5.fields import CKEditor5Field
from sorl.thumbnail import get_thumbnail

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
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.noticeTitle

class Gallery(models.Model):

    galleryName = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(default=timezone.now)


    def __str__(self):
        return self.galleryName
class Image(models.Model):
    gallery = models.ForeignKey(Gallery,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')  
    def thumbnail_url(self):
        return get_thumbnail(self.image, '300x200', crop='center', quality=90).url

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    def __str__(self):
        return self.title


class Menu(models.Model):
    menuItem = models.CharField(max_length=200, blank=False, null=False)
    menuPath = models.CharField(max_length=100)
    is_expandable = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return self.menuItem
class SubMenu(models.Model):
    menuRef = models.ForeignKey(Menu,on_delete=models.CASCADE, blank=False,null=False)
    submenu = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.submenu
    
class Message(models.Model):

    message = models.TextField()
    image = models.ImageField(upload_to='message_board/')
    is_active = models.BooleanField(default=True)

class Sliders(models.Model):
    title = models.CharField(max_length=200, null=True,blank=True)
    image = models.ImageField(upload_to="sliders/")
    is_active = models.BooleanField(default=True)

class Dynamic(models.Model):
    title = models.CharField(max_length=100)
    body =  CKEditor5Field(config_name='extends')
    image = models.ImageField(upload_to="dynamic/images/")
    files = models.FileField(upload_to='dynamic/files/')
    path = models.SlugField(unique=True, blank=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args,**kwargs)

    
    def __str__(self):
        return self.title





