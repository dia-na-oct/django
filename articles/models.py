from django.db import models

# Create your models here.
class Article(models.Model):
    title=models.CharField(max_length=30)
    slug=models.SlugField()
    body=models.TextField()
    date=models.DateTimeField(auto_now_add=True)
    def __str__(self):
      return self.title
    
    def snippet(self):
       return self.body[:50]+'....'
    


class YourModel(models.Model):
    # Your model fields go here
    name = models.CharField(max_length=255)
    description = models.TextField()
    

    def __str__(self):
        return self.name

