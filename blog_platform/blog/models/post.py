from django.db import models
from datetime import datetime


class Post(models.Model):
    title = models.CharField(max_length=128)
    content = models.TextField()
    author = models.ForeignKey("Author", on_delete=models.CASCADE)
    categories = models.ManyToManyField("Category")
    created_at = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.title
