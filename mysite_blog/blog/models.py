from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.utils.text import slugify


class ContactRequest(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=150)
    text = models.TextField()
    def __str__(self):
        return self.name


class Post(models.Model):

    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(allow_unicode=True, unique=True)

    def save(self,*args, **kwargs):
        self.slug = slugify(self.title)
        self.published_date = timezone.now()
        super().save(*args, **kwargs)

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

    def get_absolute_url(self):
        return reverse("post_detail",kwargs={"slug": self.slug})


    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey('blog.Post', related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    slug = models.SlugField(allow_unicode=True, unique=True)

    def approve(self,*args,**kwargs):

        self.slug = slugify(self.author)
        self.approved_comment = True
        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.text

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User)

    def __str__(self):
        return self.user.username
