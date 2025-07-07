import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_book_was_added(self):
        collector = BooksCollector()
        collector.add_new_book('Дом в котором')
        books = collector.get_book_genre()

        assert 'Дом в котором' in books

    def test_add_new_book_with_forty_symbols_added(self):
        collector = BooksCollector()
        collector.add_new_book('Этим утром я решила перестать есть и ...')
        books = collector.get_book_genre()

        assert 'Этим утром я решила перестать есть и ...' in books

    def test_add_new_book_with_forty_two_symbols_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Жареные зелёные помидоры в кафе Полустанок')
        books = collector.get_book_genre()

        assert 'Жареные зелёные помидоры в кафе Полустанок' not in books

    def test_add_new_book_with_zero_symbols_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('')
        books = collector.get_book_genre()

        assert '' not in books

    def test_add_new_book_second_time_not_added_twice(self):
        collector = BooksCollector()
        collector.add_new_book('Мы в это время')
        collector.add_new_book('Мы в это время')
        
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Они скоро умрут')
        collector.set_book_genre('Они скоро умрут', 'Фантастика')

        assert collector.get_book_genre('Они скоро умрут') == 'Фантастика'    

    def test_set_book_genre_not_sets_if_book_not_in_books_genre(self):
        collector = BooksCollector()
        collector.set_book_genre('Шерлок Хоумс', 'Детектив')

        assert 'Шерлок Хоумс' not in collector.get_book_genre()

    def test_set_book_genre_with_unexistent_genre_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Дятел')
        collector.set_book_genre('Дятел', 'Триллеры')

        assert 'Дятел' not in collector.get_book_genre()  

    def test_get_specific_genre_book_detective(self):
        collector = BooksCollector()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Детективы')
        collector.add_new_book('Под лестницей')
        collector.set_book_genre('Под лестницей', 'Детективы')

        specific_genre_books = collector.get_books_with_specific_genre('Детективы')

        assert specific_genre_books == ['Книга', 'Под лестницей']

    def test_get_books_with_specific_genre_filterd_to_genres(self):
        collector = BooksCollector()
        collector.add_new_book('Море цветов')
        collector.set_book_genre('Фантастика')
        collector.add_new_book('Битва')
        collector.set_book_genre('Ужасы')

        specific_genre_book_fantastic = collector.get_books_with_specific_genre('Фантастика')
        specific_genre_book_horrors = collector.get_books_with_specific_genre('Ужасы')

        assert specific_genre_book_fantastic == ['Море цветов']
        assert specific_genre_book_horrors == ['Ужасы']

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book('Мир')
        collector.set_book_genre('Мир', 'Комедия')

        books = collector.get_books_genre()

        assert 'Мир' in books

    def test_add_books_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Зомби-ленд')
        collector.add_book_in_favorites('Зомби-ленд')

        assert 'Зомби-ленд' in collector.get_list_of_favorites_books()

    def test_add_not_existed_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_book_in_favorites('Словарь')

        assert 'Словарь' not in collector.get_list_of_favorites_books()

    def test_add_books_in_favorites_second_time_not_added(self):
        collector = BooksCollector()
        collector.add_new_book('Война и Мир')
        collector.add_books_in_favorites('Война и Мир')
        collector.add_books_in_favorites('Война и Мир')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_books_for_children_added(self):
        collector = BooksCollector()
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')

        children_books = collector.get_books_for_children()

        assert 'Колобок' in children_books

    def test_get_books_for_children_age_rating(self):
        collector = BooksCollector()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        children_books = collector.get_books_for_children()

        assert 'Оно' not in children_books

    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book('Наше время')
        collector.add_book_in_favorites('Наше время')

        collector.delete_book_from_favorites('Наше время')

        assert 'Наше время' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book('Перепись')
        favorites = collector.get_list_of_favorites_books()

        assert favorites == ['Перепись']

    def test_not_get_list_of_favorites_without_favorites(self):
        collector = BooksCollector()
        favorites = collector.get_list_of_favorites_books()

        assert favorites == []    

    @pytest.mark.parametrize('name, genre',
        [
            ('Если все коты в мире исчезнут', 'Ужасы'),
            ('Она и её кот', 'Детективы')
        ]
        )

    def test_get_book_genre(name, genre):
        collector = BooksCollector()
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)
        assert collector.get_book_genre(name) == genre
