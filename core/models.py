from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models
from django.contrib.auth import get_user_model
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.urls import reverse


class GetMeta(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, )
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'profile_user' )
    telephone_number = models.IntegerField()
    region = models.CharField(max_length = 50)
    age = models.IntegerField()
    face_photo = models.ImageField(upload_to='meta face/')

class ActiveMeta(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'meta_user')
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, related_name = 'meta_user_profile')
    metas = models.BooleanField(default = False)


class ContentUploud_Model(models.Model):
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='content_uplouds_user_profile')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='content_uplouds_user')
    content_title = models.CharField(max_length=150)
    content = models.ImageField(upload_to='user_content/')
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='post_likes', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    viewer = models.PositiveIntegerField((), null=True)

    def __str__(self):
        return self.content_title

    class Meta:
        ordering = ['-created_at']



class UserProfileSeeModel(AbstractUser):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE, null=True)
    profile_image = models.ImageField(upload_to='profile_photo/', null=True)
    subscribers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='subscribes', blank=True, null=True)
    actived = models.BooleanField(default=False)
    add_to_friend  = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='add_user_to_friend')
    meta_active = models.ForeignKey(ActiveMeta , on_delete = models.CASCADE, related_name = 'get_meta_activet_user', null=True)


class Comment(models.Model):
    content = models.ForeignKey(ContentUploud_Model, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments_user', null=True)
    user_profile = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, related_name='comments_user_profile')
    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.CharField(max_length=50)
    like = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='commnetrion_like', null=True)


    def __str__(self):
        return self.comment


