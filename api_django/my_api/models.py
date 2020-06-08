from django.db import models

# новости, заголовок и ссылк
class News(models.Model):
    title = models.TextField()
    url = models.URLField()

    def __str__(self):
        return self.title


