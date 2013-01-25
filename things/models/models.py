from django.db import models

# Create your models here.
class Note(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    createtime = models.DateTimeField()
    modifytime = models.DateTimeField()
    flag = models.SmallIntegerField()
    
    def __unicode__(self):
        return self.title
    
    class Meta:
        ordering = ['-modifytime']
        