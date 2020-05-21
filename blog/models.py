from django.db import models

#create blog model
#title
#pub_date
#body
#image

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
    
#add blog to settings

