from email.mime import image
from gc import DEBUG_COLLECTABLE
from pyexpat import model
from django import db
from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.


class Post(models.Model):
    class Mata(object):
        db_table = 'posts'

    name = models.CharField(
        'name', blank=False, null=False, max_length=14, db_index=True, default='Anonymous'
    )
    body = models.CharField(
        'body', blank=True, null=True, db_index=True, max_length=140
    )
    created_at = models.DateTimeField(
        'created DateTime', blank=True, auto_now_add=True
    )
    image = CloudinaryField(
        'image',blank=True,db_index=True
    )
    like_count = models.PositiveBigIntegerField(
        'like_count',default=0,blank=True
    )
