from django.db import models

# Create your models here.
class Posts(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    description = models.TextField(null=False, blank=False)
    date_created = models.DateTimeField()
    author = models.CharField(max_length=100, null=False, blank=False)
    date_updated = models.DateTimeField()

    def __str__(self):
        return self.name + ' by ' + self.author


