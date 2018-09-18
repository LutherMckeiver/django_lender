from django.db import models
import datetime


class Book(models.Model):
    STATUS = [
        ("available", "Available"),
        ("checked-out", "Checked-Out"),
    ]
    title = models.CharField(max_length=48)
    author = models.CharField(max_length=48)
    year = models.DateField()
    status = models.CharField(choices=STATUS, default='available', max_length=48)
    date_added = models.DateTimeField(auto_now_add=True)
    last_borrowed = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'{self.title} {self.author} {self.year} {self.status} {self.date_added}'
