from django.db import models

class Quote(model.Models):
    character = models.CharField(max_length=64)
    line = models.CharField(max_length=1024)

    def __str__(self):
        return 'CHARACTER: {}/nLINE: {}'.format(self.character, self.quote)