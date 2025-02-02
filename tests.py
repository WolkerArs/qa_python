import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize('name', ['Свет в конце лабиринта стальных дорог три',
                                      'Свет в конце лабиринта стальных дорог триж',
                                      'Свет в конце лабиринта стальных дорог трижды'])
    def test_add_new_book_add_book_with_more_then_40symbols_not_added(self, name):
        collector = BooksCollector()
        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_add_new_book_add_book_second_time_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Преступление и Наказание')
        collector.add_new_book('Преступление и Наказание')

        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre_genre_in_list_is_set(self):
        collector = BooksCollector()
        collector.add_new_book('Кровавый Меридиан')
        collector.set_book_genre('Кровавый Меридиан', 'Ужасы')

        assert collector.get_books_genre()['Кровавый Меридиан'] == 'Ужасы'

    def test_set_book_genre_unknown_genre_is_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Яма')
        collector.set_book_genre('Яма', 'Драма')

        assert collector.books_genre['Яма'] == ''

    def test_set_book_genre_unknown_book_is_not_set(self):
        collector = BooksCollector()
        collector.add_new_book('Яма')
        collector.add_new_book('Бесы')
        collector.set_book_genre('Анна Каренина', 'Комедии')

        assert len(collector.books_genre) == 2 and "Комедии" not in collector.books_genre.values()

    def test_get_book_genre_get_one_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')

        assert collector.get_book_genre('12 стульев') == 'Комедии'

    def test_get_books_with_specific_genre_choose_known_genre_get_list_of_books(self):
        collector = BooksCollector()
        collector.add_new_book('Кровавый Меридиан')
        collector.add_new_book('Преступление и Наказание')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('Кровавый Меридиан', 'Ужасы')
        collector.set_book_genre('Преступление и Наказание', 'Ужасы')
        collector.set_book_genre('12 стульев', 'Комедии')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Кровавый Меридиан',
                                                                    'Преступление и Наказание']

    def test_get_books_with_specific_genre_choose_unknown_genre_get_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Кровавый Меридиан')
        collector.add_new_book('Преступление и Наказание')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('Кровавый Меридиан', 'Ужасы')
        collector.set_book_genre('Преступление и Наказание', 'Ужасы')
        collector.set_book_genre('12 стульев', 'Комедии')

        assert collector.get_books_with_specific_genre('Драмы') == []

    def test_get_books_genre_get_dictionary_three_books(self):
        collector = BooksCollector()
        collector.add_new_book('Кровавый Меридиан')
        collector.add_new_book('Преступление и Наказание')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('12 стульев', 'Комедии')

        assert collector.get_books_genre() == {'Кровавый Меридиан': '',
                                               'Преступление и Наказание': '',
                                               '12 стульев': 'Комедии'}

    def test_get_books_for_children_three_books_get_list_without_age_rating_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Кровавый Меридиан')
        collector.add_new_book('Преступление и Наказание')
        collector.add_new_book('12 стульев')
        collector.set_book_genre('Кровавый Меридиан', 'Ужасы')
        collector.set_book_genre('Преступление и Наказание', 'Детективы')
        collector.set_book_genre('12 стульев', 'Комедии')

        assert collector.get_books_for_children() == ['12 стульев']

    def test_get_books_for_children_no_children_books_get_empty_list(self):
        collector = BooksCollector()
        collector.add_new_book('Кровавый Меридиан')
        collector.add_new_book('Преступление и Наказание')
        collector.set_book_genre('Кровавый Меридиан', 'Ужасы')
        collector.set_book_genre('Преступление и Наказание', 'Детективы')

        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_add_one_book(self):
        collector = BooksCollector()
        collector.add_new_book('Кровавый Меридиан')
        collector.add_book_in_favorites('Кровавый Меридиан')

        assert collector.get_list_of_favorites_books() == ['Кровавый Меридиан']

    def test_add_book_in_favorites_add_unknown_book_is_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Кровавый Меридиан')
        collector.add_book_in_favorites('Кровавый Меридиан')
        collector.add_book_in_favorites('Бесы')

        assert collector.get_list_of_favorites_books() == ['Кровавый Меридиан']

    def test_delete_book_from_favorites_one_book_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Кровавый Меридиан')
        collector.add_book_in_favorites('Кровавый Меридиан')
        collector.delete_book_from_favorites('Кровавый Меридиан')

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_book_not_in_list_is_not_deleted(self):
        collector = BooksCollector()
        collector.add_new_book('Кровавый Меридиан')
        collector.add_new_book('Бесы')
        collector.add_book_in_favorites('Кровавый Меридиан')
        collector.delete_book_from_favorites('Бесы')

        assert (collector.get_list_of_favorites_books() == ['Кровавый Меридиан']
                and len(collector.get_books_genre()) == 2)

    def test_get_list_of_favorites_books_three_books_get_list(self):
        collector = BooksCollector()
        books = ['Кровавый Меридиан', 'Преступление и Наказание', '12 стульев']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)

        assert len(collector.get_list_of_favorites_books()) == 3

    def test_get_list_of_favorites_books_three_books_one_deleted_get_list_two_books(self):
        collector = BooksCollector()
        books = ['Кровавый Меридиан', 'Преступление и Наказание', '12 стульев']
        for book in books:
            collector.add_new_book(book)
            collector.add_book_in_favorites(book)
        collector.delete_book_from_favorites('12 стульев')

        assert collector.get_list_of_favorites_books() == ['Кровавый Меридиан',
                                                           'Преступление и Наказание']
