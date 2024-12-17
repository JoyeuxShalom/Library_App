
from django.db import models
from django.utils import timezone

# Book Model
class Book(models.Model):
    isbn = models.CharField(max_length=13, unique=True)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    rack_number = models.CharField(max_length=10)
    total_copies = models.IntegerField(default=1)
    available_copies = models.IntegerField(default=1)
    usage_statistics = models.IntegerField(default=0)

    def __str__(self):
        return self.title

# Member Model
class Member(models.Model):
    MEMBER_TYPES = [
        ('UG', 'Undergraduate'),
        ('PG', 'Postgraduate'),
        ('RS', 'Research Scholar'),
        ('FC', 'Faculty'),
    ]

    member_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    member_type = models.CharField(max_length=2, choices=MEMBER_TYPES)
    issued_books = models.ManyToManyField('Book', through='Transaction')

    def max_books_allowed(self):
        return {'UG': 2, 'PG': 4, 'RS': 6, 'FC': 10}[self.member_type]

    def __str__(self):
        return self.name

# Transaction Model
class Transaction(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    issue_date = models.DateField(default=timezone.now)
    due_date = models.DateField()
    return_date = models.DateField(null=True, blank=True)
    penalty = models.FloatField(default=0.0)

    def calculate_penalty(self):
        if self.return_date and self.return_date > self.due_date:
            overdue_days = (self.return_date - self.due_date).days
            self.penalty = overdue_days * 10  # Penalty rate: 10 units per day
            return self.penalty
        return 0.0

