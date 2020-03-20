from django.db import models
from django.contrib.auth.models import User
import os


class CloudFile(models.Model):
    description = models.CharField(max_length=255, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    fileName = models.CharField(max_length=1000, blank=False)

    def filename(self):
        return os.path.basename(self.file.name)


# Create your models here.
1
