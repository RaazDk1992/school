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

class ContentType(models.Model):
    contentType = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    def __str__(self):
        return self.contentType
    

class Notices(models.Model):
    title = models.CharField(max_length=200)
    body = CKEditor5Field(config_name='extends')
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class NoticeImages(models.Model):
    notice = models.ForeignKey(Notices,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='notices/images/',blank=True,null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.notice
    
class NoticeDocuments(models.Model):
    notice = models.ForeignKey(Notices,on_delete=models.CASCADE)
    document =models.FileField(upload_to='notices/documents/', blank=True, null=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.notice
    




class Gallery(models.Model):

    galleryName = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    creation_date = models.DateField(default=timezone.now)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.galleryName
    
class Events(models.Model):
    date_en = models.DateField()
    date_np = models.CharField(max_length=20)
    event = models.CharField(max_length=200)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.event

class Testimonials(models.Model):
    name = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='testimonial/images/')
    extra = models.CharField(max_length=200)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    
class Image(models.Model):
    gallery = models.ForeignKey(Gallery,on_delete=models.CASCADE)
    image = models.ImageField(upload_to='gallery_images/')  
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def thumbnail_url(self):
        return get_thumbnail(self.image, '300x200', crop='center', quality=90).url
    


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    image = models.ImageField(upload_to='articles/', null=True, blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.title


class Menu(models.Model):
    menuItem = models.CharField(max_length=200, blank=False, null=False)
    menuPath = models.CharField(max_length=100)
    contentType = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    viewRef =  models.CharField(max_length=100)
    is_expandable = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    
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
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

class Sliders(models.Model):
    title = models.CharField(max_length=200, null=True,blank=True)
    image = models.ImageField(upload_to="sliders/")
    is_active = models.BooleanField(default=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)

class Dynamic(models.Model):
    contentType = models.ForeignKey(ContentType,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    body =  CKEditor5Field(config_name='extends')
    image = models.ImageField(upload_to="dynamic/images/", null=True,blank=True)
    document = models.FileField(upload_to='dynamic/files/',null=True,blank=True)
    path = models.SlugField(unique=True, blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE)
    def save(self, *args, **kwargs):
        if not self.path:
            self.path = slugify(self.title)
        super().save(*args,**kwargs)
    
    def __str__(self):
        return self.title





