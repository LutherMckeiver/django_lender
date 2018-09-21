from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list_view(request):
    """
    :param request:
    :return: A list of all Books rendered in HTML
    """
    books = Book.objects.filter(user__username=request.user.username)
    context = {
        'books': books
    }

    return render(request, 'books/book_list.html', context=context)


def book_detail_view(request, pk=None):
    """
    :param request:
    :param pk:
    :return: A 404 if book is not found otherwise returns individual book detail
    """
    book = get_object_or_404(Book, id=pk, user__username=request.user.username)
    context = {
        'book': book,
    }
    return render(request, 'books/book_detail.html', context)
