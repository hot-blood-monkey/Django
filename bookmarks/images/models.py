from django.db import models
from django.conf import settings

# Create your models here.
from django.utils.text import slugify


class Image(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,related_name='images_created',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    image = models.ImageField(upload_to='images/%y/%m/%d')
    description = models.TextField(blank=True)
    created = models.DateField(auto_now_add=True,db_index=True)

    user_like = models.ManyToManyField(settings.AUTH_USER_MODEL,
                                       related_name='imaged_liked',
                                       blank=True)

    def __str__(self):
        return self.title

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Image,self).save(*args,**kwargs)