from django.db import models

# Create your models here.
class Topic(models.Model):
    topic=models.CharField(max_length=50,primary_key=True)

    def __str__(self):
        return self.topic

class Webpage(models.Model):
    topic=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100,primary_key=True)
    url=models.URLField(unique=True)

    def __str__(self):
        return self.name

class Access_Details(models.Model):
    web_name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()

    def __str__(self):
        return str(self.web_name)
    
    
    