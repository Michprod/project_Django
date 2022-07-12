from django.db import models

class Film(models.Model):
      title = models.CharField(max_length=50)
      description = models.TextField()
      image = models.ImageField(upload_to = 'film_pic')

      def __str__(self):
          return self.title  