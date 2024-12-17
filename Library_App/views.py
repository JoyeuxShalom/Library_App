
from django.shortcuts import render, redirect
from .models import Book, Member, Transaction
from datetime import timedelta, date


# Display all books
def book_list(request):
    books = Book.objects.all()
    return render(request, 'library_app/book_list.html', {'books': books})


# Add a new book
def add_book(request):
    if request.method == 'POST':
        title = request.POST['title']
        author = request.POST['author']
        isbn = request.POST['isbn']
        rack_number = request.POST['rack']
        copies = int(request.POST['copies'])
        Book.objects.create(title=title, author=author, isbn=isbn, rack_number=rack_number, total_copies=copies,
                            available_copies=copies)
        return redirect('book_list')
    return render(request, 'library_app/add_book.html')


# Issue a book
def issue_book(request):
    members = Member.objects.all()
    books = Book.objects.filter(available_copies__gt=0)

    if request.method == 'POST':
        member_id = request.POST['member']
        isbn = request.POST['book']
        member = Member.objects.get(pk=member_id)
        book = Book.objects.get(pk=isbn)

        if member.issued_books.count() < member.max_books_allowed():
            due_date = date.today() + timedelta(days=30)  # 1-month borrowing
            Transaction.objects.create(book=book, member=member, due_date=due_date)
            book.available_copies -= 1
            book.save()
        return redirect('book_list')

    return render(request, 'library_app/issue_book.html', {'members': members, 'books': books})

