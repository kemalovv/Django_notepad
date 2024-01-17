from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    """Subject of the user study"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Returning str representation of a model"""
        return self.text


class Entry(models.Model):
    """Information that user has studied"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"

    def __str__(self):
        """Returning str representation of a model"""
        if len(self.text) > 50:
            return f"{self.text[:50]}..."
        return self.text
