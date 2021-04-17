from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    intro = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering = ['-date_added']


class Comment(models.Model):
    post =models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)
    body = models.TextField()

    class Meta:
        ordering =['date_added']
