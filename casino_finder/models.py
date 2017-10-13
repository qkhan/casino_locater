from django.db import models

# Create your models here.
class Casino(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'Casino'

    def __str__(self):
        return '[{0}-{1}]'.format(self.__class__.__name__, self.id)
