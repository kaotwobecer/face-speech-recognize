from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class UserProfile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    speech = models.CharField(max_length=512, null=False)
    picture_1 = models.CharField(max_length=512, null=False)
    picture_2 = models.CharField(max_length=512, null=True)
    picture_3 = models.CharField(max_length=512, null=True)
    picture_4 = models.CharField(max_length=512, null=True)
    picture_5 = models.CharField(max_length=512, null=True)
    picture_6 = models.CharField(max_length=512, null=True)
    picture_7 = models.CharField(max_length=512, null=True)
    picture_8 = models.CharField(max_length=512, null=True)
    picture_9 = models.CharField(max_length=512, null=True)
    picture_10 = models.CharField(max_length=512, null=True)
    picture_11 = models.CharField(max_length=512, null=True)
    picture_12 = models.CharField(max_length=512, null=True)
    picture_13 = models.CharField(max_length=512, null=True)
    picture_14 = models.CharField(max_length=512, null=True)
    picture_15 = models.CharField(max_length=512, null=True)
    picture_16 = models.CharField(max_length=512, null=True)
    picture_17 = models.CharField(max_length=512, null=True)
    picture_18 = models.CharField(max_length=512, null=True)
    picture_19 = models.CharField(max_length=512, null=True)
    picture_20 = models.CharField(max_length=512, null=True)

    def __str__(self):
        return self.user_id
