from django.db import models

# Create your models here.
class Document(models.Model):

    description = models.CharField(max_length=255, blank=True)
    imagefile = models.FileField(upload_to='uploads')
    reg_dt = models.DateTimeField(auto_now_add=True)