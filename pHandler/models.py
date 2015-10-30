from django.db import models


# Create your models here.
class PHandler(models.Model):
    name = models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

    class Meta:
        # The default permission
        # https://docs.djangoproject.com/en/1.8/ref/models/options/
        default_permissions = ('add', 'change', 'delete', 'view')
