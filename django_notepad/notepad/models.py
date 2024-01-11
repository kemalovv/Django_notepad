from django.db import models


class Topic(models.Model):
    """Subject of the user study"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Returning str representation of a model"""
        return self.text
