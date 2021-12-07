from django.db import models

'''
Category
===========
title, slug

Tags
=======
title, slug

Post
========
title, slug, author, content, created_at, photo, views, category, tags
'''


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url_category', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Tags(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50, verbose_name='Url_slug', unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['title']


class Post(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, verbose_name='Url_category', unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Опубликовано')
    photo = models.ImageField(upload_to='photo/%Y/%m/%d/', blank=True)
    views = models.IntegerField(default=0, verbose_name='Кол-во просмотров')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='posts')
    tags = models.ManyToManyField(Tags, blank=True, related_name='posts')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']


