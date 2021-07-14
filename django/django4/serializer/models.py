import uuid
from django.db import models

class Book(models.Model):
    class Meta:
        ordering = ['created_at']

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=20)
    price = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
