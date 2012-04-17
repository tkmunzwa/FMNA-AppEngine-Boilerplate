from django.db import models

class Ujinga(models.Model):
    content = models.TextField(max_length = 1000)

    def __unicode__(self):
        return self.content[:10]
