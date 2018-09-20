from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list_view(request):
    if not request.user.is_authenticated:
        return render(request, 'base/base.html', status=403)
    books = Book.objects.all()

    context = {
        'books': books
    }

    return render(request, 'books/book_list.html', context=context)


def book_detail_view(request, pk=None):
    single_book = Book.objects.get(pk)

    context = {
        'book id': single_book
    }

    return render(request, 'books/book_detail.html', context=context)
