from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    overview = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    
    thumbnail = models.ImageField()
    
    featured = models.BooleanField()

    def __str__(self):
        return self.title