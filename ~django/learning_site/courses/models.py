from django.db import models

# Create your models here.
class Course(models.Model):
    created_at = models.DateTimeField(auto_now_add = True)
    title = models.CharField(max_length = 256)
    description = models.CharField(max_length = 255, default='DEFAULT VALUE', blank=True, null=True )
    #new_field = models.TextField(max_length=140, default='DEFAULT VALUE', blank=True, null=True)

    def __str__(self):
        return self.title


def __unicode__(self):
    return self.title
    return self.description

class Step(models.Model):
    title = models.CharField(max_length = 255)
    description =  models.CharField(max_length = 255, default='', blank=True, null=True )
    content = models.TextField( default='', blank=True, null=True )
    order = models.IntegerField(default = 0)
    course = models.ForeignKey('course',   on_delete=models.CASCADE)

    class meta:
        ordering = ['order',]

    def __str__(self):
        return self.title
