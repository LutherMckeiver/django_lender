from django.test import TestCase, RequestFactory
from .models import Book
# Create your tests here.


class TestBookModel(TestCase):
    def setUp(self):
        self.book = Book.objects.create(title='Hello', author='Goodbye')
        Book.objects.create(title='Desk', author='Chair')
        Book.objects.create(title='Wall', author='Whiteboard')

    def test_book_titles(self):
        self.assertEqual(self.book.title, 'Hello')

    def test_book_author(self):
        self.assertEqual(self.book.author, 'Goodbye')

    def test_wrong_title(self):
        book = Book.objects.get(author='Chair')

        self.assertEqual(book.title, 'Desk')

    def test_wrong_author(self):
        book = Book.objects.get(author='Wall')

        self.assertEqual(book.author, 'Whiteboard')


class TestBookViews(TestCase):
    def setUp(self):
        self.request = RequestFactory()
        self.book_one = Book.objects.create(title='Cool', author='Omg wow')
        self.book_two = Book.objects.create(title='Beans', author='Jelly Beans')

    def test_book_detail_view(self):
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{self.book_one.id}')
        self.assertIn(b'Omg wow', response.content)

    def test_book_detail_status(self):
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{self.book_one.id}')
        self.assertEqual(200, response.status_code)
