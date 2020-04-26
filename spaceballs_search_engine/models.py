from django.db import models

class Quote(models.Model):
    character = models.CharField(max_length=64)
    line = models.CharField(max_length=1024)

    def __str__(self):
        return '{}--{}'.format(self.character, self.line)