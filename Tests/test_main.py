import requests
import main
import pytest


@pytest.mark.parametrize(
    'side1, side2, side3, expected',
    (
        [1, 145, 145, 'Равнобедренный треугольник'],
        [10, 10, 10, 'Равносторонний треугольник'],
        [-10, 10, 20, 'Треугольник не существует']
    )
)
def test_check_triangle(side1, side2, side3, expected):
    actual = main.check_triangle(side1, side2, side3)
    assert actual == expected


@pytest.mark.parametrize(
    'film_1, film_2, film_3, expected',
    (
        ['Аладин', 'Мадагаскар', 'Бетховен', 'Мадагаскар'],
        ['Бумер', 'Бумер: Фильм второй', 'Бумеранг', 'Бумер: Фильм второй'],
        ['Железный Человек', 'Стражи Галактики', 'Капитан Америка', 'Железный Человек']
    )
)
def test_longest_film(film_1, film_2, film_3, expected):
    actual = main.longest_film(film_1, film_2, film_3)
    assert actual == expected


@pytest.mark.parametrize(
    'list_, expected',
    (
        [['Иванов', 'Иван', 'Иванович'], 'ИИИ'],
        [['Жан', 'Клот', 'Вандамович'], 'ЖКВ'],
        [['Павлов', 'Иван', 'Уралович'], 'ПИУ']
    )
)
def test_fio(list_, expected):
    actual = main.fio(list_)
    assert actual == expected


class TestYandexDisk:
    def setup_method(self):
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth lalala'
        }

    def test_create_catalog(self):
        params = {'path': 'myphoto'}
        url = f'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(url, headers=self.headers, params=params)
        assert response.status_code == 201

    def test_create_catalog_409(self):
        params = {'path': 'myphoto'}
        url = f'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(url, headers=self.headers, params=params)
        assert response.status_code == 409

    def test_create_catalog_400(self):
        params = {}
        url = f'https://cloud-api.yandex.net/v1/disk/resources'
        response = requests.put(url, headers=self.headers, params=params)
        assert response.status_code == 400

