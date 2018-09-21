from django.db import models
from django.contrib.auth.models import User


class Book(models.Model):
    STATUS = [
        ("available", "Available"),
        ("checked-out", "Checked-Out"),
    ]
    title = models.CharField(max_length=48)
    year = models.DateField(blank=True, null=True)
    status = models.CharField(choices=STATUS, default='available', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='book')
    author = models.CharField(max_length=48)

    def __str__(self):
        return f' Book: {self.title}'

    def __repr__(self):
        return f' Book: {self.title} {self.author} {self.year} {self.status} {self.date_added}'
