from django.db import models
from django.db.models import Model


class Posts(Model):
    text = models.TextField()

    def __str__(self):
        return f"Post model: {self.text[:50]}"
