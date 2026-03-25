from django.db import models
from tinymce.models import HTMLField
from .helpers import *  # noqa: F403


# Create your models here.
class Category(models.Model):
    LAYOUT_CHOICE = (
        ("list", "List"),
        ("grid", "Grid"),
    )
    STATUS_CHOICE = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    is_homepage = models.BooleanField(default=False)
    layout = models.CharField(max_length=10, choices=LAYOUT_CHOICE, default="list")
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="draft")
    ordering = models.IntegerField(default=0)

    def __str__(self):
        return self.name


class Artical(models.Model):
    STATUS_CHOICE = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="draft")
    ordering = models.IntegerField(default=0)
    special = models.BooleanField(default=False)
    publish_date = models.DateTimeField()
    content = HTMLField()
    image = models.ImageField(upload_to=get_file_path)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Feed(models.Model):
    STATUS_CHOICE = (
        ("draft", "Draft"),
        ("published", "Published"),
    )
    name = models.CharField(unique=True, max_length=100)
    slug = models.SlugField(unique=True, max_length=100)
    status = models.CharField(max_length=10, choices=STATUS_CHOICE, default="draft")
    ordering = models.IntegerField(default=0)
    link = models.CharField(max_length=250)

    def __str__(self):
        return self.name
