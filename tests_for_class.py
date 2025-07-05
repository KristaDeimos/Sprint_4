class BooksCollector:

    def __init__(self):
        self.books_genre = {}
        self.favorites = []
        self.genre = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
        self.genre_age_rating = ['Ужасы', 'Детективы']
    
    # добавляем новую книгу
    def add_new_book(self, name):
        if not self.books_genre.get(name) and 0 < len(name) < 41:
            self.books_genre[name] = ''

    # устанавливаем книге жанр 
    def set_book_genre(self, name, genre):
        if name in self.books_genre and genre in self.genre:
            self.books_genre[name] = genre

    # получаем жанр книги по её имени
    def get_book_genre(self, name):
        return self.books_genre.get(name)

    # выводим список книг с определённым жанром
    def get_books_with_specific_genre(self, genre):
        books_with_specific_genre = []
        if self.books_genre and genre in self.genre:
            for name, book_genre in self.books_genre.items():
                if book_genre == genre:
                    books_with_specific_genre.append(name)
        return books_with_specific_genre

    # получаем словарь books_genre
    def get_books_genre(self):
        return self.books_genre

    # возвращаем книги, подходящие детям
    def get_books_for_children(self):
        books_for_children = []
        for name, genre in self.books_genre.items():
            if genre not in self.genre_age_rating and genre in self.genre:
                books_for_children.append(name)
        return books_for_children

    # добавляем книгу в Избранное
    def add_book_in_favorites(self, name):
        if name in self.books_genre:
            if name not in self.favorites:
                self.favorites.append(name)

    # удаляем книгу из Избранного
    def delete_book_from_favorites(self, name):
        if name in self.favorites:
            self.favorites.remove(name)

    # получаем список Избранных книг
    def get_list_of_favorites_books(self):
        return self.favorites 


import pytest
from main import BooksCollector

class TestBooksCollector:

    def test_add_new_book_book_is_added(self):
        collector = BooksCollection()
        collector.add_new_book('Дом в котором')
        books = collector.get_book_genre()

        assert 'Дом в котором' in books

    def test_add_new_book_have_no_genre(self):
        collector = BooksCollection()
        collection.add_new_book('Ветролом')

        assert 'Ветролом' not in books_genre

    def test_add_new_book_with_one_symbol_added(self):
        collector = BooksCollection()
        collector.add_new_book('А')
        books = collector.get_book_genre()

        assert 'А' in books

    def test_add_new_book_with_twenty_symbols_added(self):
        collector = BooksCollection()
        collector.add_new_book('Цветы для Элджернона')
        books = collector.get_book_genre()

        assert 'Цветы для Элджернона' in books

    def test_add_new_book_with_thirty_nine_symbols_added(self):
        collector = BooksCollection()
        collector.add_new_book('Дай вам Бог здоровья, мистер Розутер...') 
        books = collector.get_book_genre()

        assert 'Дай вам Бог здоровья, мистер Розутер...' in books

    def test_add_new_book_with_forty_symbols_added(self):
        collector = BooksCollection()
        collector.add_new_book('Этим утром я решила перестать есть и ...')
        books = collector.get_book_genre()

        assert 'Этим утром я решила перестать есть и ...' in books

    def test_add_new_book_with_forty_two_symbols_not_added(self):
        collector = BooksCollection()
        collector.add_new_book('Жареные зелёные помидоры в кафе Полустанок')
        books = collector.get_book_genre()

        assert 'Жареные зелёные помидоры в кафе Полустанок' not in books

    def test_add_new_book_with_zero_symbols_not_added(self):
        collector = BooksCollection()
        collector.add_new_book('')
        books = collector.get_book_genre()

        assert '' not in books

    def test_add_new_book_second_time_not_added_twice(self):
        collector = BooksCollection()
        collector.add_new_book('Мы в это время')
        collector.add_new_book('Мы в это время')
        
        assert len(collector.get_books_genre()) == 1

    def test_set_book_genre(self):
        collector = BooksCollection()
        collector.add_new_book('Они скоро умрут')
        collector.set_book_genre('Они скоро умрут', 'Фантастика')

        assert collection.get_book_genre('Они скоро умрут') == 'Фантастика'    

    def test_set_book_genre_not_sets_if_book_not_in_books_genre(self):
        collector = BooksCollection()
        collector.set_book_genre('Шерлок Хоумс', 'Детектив')

        assert 'Шерлок Хоумс', not in books_genre

    def get_books_with_specific_genre_fantastic(self):
        collector = BooksCollection()
        collector.add_new_book('Ты и я')
        collector.set_book_genre('Ты и я', 'Фантастика')
        collector.add_new1-book('Твоё имя')
        collector.set_book_genre('Твоё имя', 'Фантастика')

        specific_genre_books = collector.get_books_with_specific_genre('Фантастика')

        assert specific_genre_books == ['Ты и я', 'Твоё имя']

    def get_books_with_specific_genre_horrors(self):
        collector = BooksCollection()
        collector.add_new_book('Номер 1')
        collector.set_book_genre('Номер 1', 'Ужасы')
        collector.add_new1-book('Мороз')
        collector.set_book_genre('Мороз', 'Ужасы')

        specific_genre_books = collector.get_books_with_specific_genre('Ужасы')

        assert specific_genre_books == ['Номер 1', 'Мороз']

    def get_books_with_specific_genre_detective(self):
        collector = BooksCollection()
        collector.add_new_book('Книга')
        collector.set_book_genre('Книга', 'Детективы')
        collector.add_new1-book('Под лестницей')
        collector.set_book_genre('Под лестницей', 'Детективы')

        specific_genre_books = collector.get_books_with_specific_genre('Детективы')

        assert specific_genre_books == ['Книга', 'Под лестницей']

    def get_books_with_specific_genre_cartoons(self):
        collector = BooksCollection()
        collector.add_new_book('Мы')
        collector.set_book_genre('Мы', 'Мультфильмы')
        collector.add_new1-book('Ёжики')
        collector.set_book_genre('Ёжики', 'Мультфильмы')

        specific_genre_books = collector.get_books_with_specific_genre('Мультфильмы')

        assert specific_genre_books == ['Мы', 'Ёжики']

    def get_books_with_specific_genre_comedy(self):
        collector = BooksCollection()
        collector.add_new_book('О нас')
        collector.set_book_genre('О нас', 'Комедия')
        collector.add_new1-book('Yes')
        collector.set_book_genre('Yes', 'Комедия')

        specific_genre_books = collector.get_books_with_specific_genre('Комедия')

        assert specific_genre_books == ['О нас', 'Yes']

    def test_get_books_genre(self):
        collector = BooksCollection()
        collector.add_new_book('Мир')
        collector.set_book_genre('Мир', 'Комедия')

        assert 'Мир' in books_genre

    def test_add_books_in_favorites(self):
        collector = BooksCollection()
        collector.add_new_book('Зомби-ленд')
        collector.add_book_in_favorites('Зомби-ленд')

        assert 'Зомби-ленд' in collector.get_list_of_favorites_books()

    def test_add_not_existed_book_in_favorites(self):
        collector = BooksCollection()
        collector.add_book_in_favorites('Словарь')

        assert 'Словарь' not in collector.get_list_of_favorites_books()

    def test_add_books_in_favorites_second_time_not_added(self):
        collector = BooksCollection()
        collector.add_new_book('Война и Мир')
        collector.add_books_in_favorites('Война и Мир')
        collector.add_books_in_favorites('Война и Мир')

        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_books_for_children_added(self):
        collector = BooksCollection()
        collector.add_new_book('Колобок')
        collector.set_book_genre('Колобок', 'Мультфильмы')

        children_books = collector.get_books_for_children()

        assert 'Колобок' in choldren_books

    def test_get_books_for_children_age_rating(self):
        collector = BooksCollection()
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')

        children_books = collector.get_books_for_children()

        assert 'Оно' not in children_books

    def test_delete_book_from_favorites(self):
        collector = BooksCollection()
        collector.add_new_book('Наше время')
        collector.add_book_in_favorites('Наше время')

        collector.delete_book_from_favorites('Наше время')

        assert 'Наше время' not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self):
        collector = BooksCollection()
        collector.add_new_book('Перепись')
        favorites = collector.get_list_of_favorites_books()

        assert favorites == ['Перепись']

    def test_not_get_list_of_favorites_without_favorites(self):
        collector = BooksCollection()
        favorites = collector.get_list_of_favorites_books()

        assert favorites = [] 
