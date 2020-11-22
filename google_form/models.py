from django.db import models

# Create your models here.


class GoogleForm(models.Model):
    title = models.CharField(max_length=255)
    submit_deadline = models.DateTimeField()
    embed_url = models.TextField()

    def __str__(self):
        return self.title

