from django.test import TestCase, RequestFactory
from .models import Book
from django.contrib.auth.models import User


class TestBookModel(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='test', email='testemail@gmail.com')
        self.user.set_password('dudebroguyman')
        self.book = Book.objects.create(
            title='Django',
            author='Python',
            user=self.user
        )
        Book.objects.create(title='Late Nights At Code Fellows', author='401 Student', user=self.user)
        Book.objects.create(title='Sapiens', author='Yuval Noah Harari', user=self.user)

    def test_book_titles(self):
        """
        :return: Test if title is correct
        """
        self.assertEqual(self.book.title, 'Django')

    def test_book_author(self):
        """
        :return: Testing if author is correct
        """
        self.assertEqual(self.book.author, '401 Student')

    def test_book_detail(self):
        """
        :return: Test if book detail is correct
        """
        book = Book.objects.get(author='Yuval Noah Harari')

        self.assertEqual(book.title, 'Sapiens')


class TestBookViews(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='Peter Parker', email='imnotspiderman@spidy.com')
        self.user.set_password('maryjane')
        self.book_one = Book.objects.create(title='Lion', author='Tiger')
        self.book_two = Book.objects.create(title='Tiger', author='Lion')

    def test_book_detail_view(self):
        """
        :return: Testing the book detail view
        """
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{self.book_one.id}')
        self.assertIn(b'Tiger', response.content)

    def test_book_detail_status(self):
        """
        :return: Testing if the status is correct
        """
        from .views import book_detail_view
        request = self.request.get('')
        response = book_detail_view(request, f'{self.book_one.id}')
        self.assertEqual(200, response.status_code)
