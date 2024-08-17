from django.db import models

class Customers(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True, default=None)

    class Meta:
        db_table = 'customers'
        indexes = [
            models.Index(fields=['last_name', 'first_name']),  # Index for faster search by name
        ]
        ordering = ['last_name', 'first_name']  # Default ordering

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.email})"
