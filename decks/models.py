from django.db import models


class Deck(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True, blank=True)
    title = models.CharField(max_length=100)
    description = models.TextField()
    last_reviewed_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title
