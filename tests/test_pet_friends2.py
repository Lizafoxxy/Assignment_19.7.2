import _pytest
from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

# тест 1
def test_add_new_pet_with_valid_data_no_photo(name='Шарик', animal_type='барбос',
                                     age=5):
    """Проверяем что можно добавить питомца с корректными данными и БЕЗ фото"""

   # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_no_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

# тест 2
def test_add_photo_for_pet(pet_photo='images/tobik.jpg'):
    """Проверяем, что можно добавить фото для питомца, уже имеющегося на сайте"""

    # Получаем ключ auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Создаем питомца для теста с помощью метода без добавления фото
    test_pet = pf.add_new_pet_no_photo(auth_key, 'Фунтяшка', 'поросенок', 2)

    # Берем id созданного тестового питомца
    pet_id = test_pet[1]['id']

    # Получаем полный путь изображения питомца  и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # # Добавляем фото для созданного тестового питомца на основе его id
    status, result = pf.add_photo_of_pet(auth_key, pet_id, pet_photo)

    # Проверяем что статус ответа = 200 и что значение pet_photo в ответе не пустое
    assert status == 200
    assert result['pet_photo'] != ''

# тест 3
def test_no_symbols_in_name_new_pet(name='@#$%^', animal_type='барбос',
                                     age=5):
    """Проверяем что нельзя добавить питомца с некорректными данными в виде спецсимволов и БЕЗ фото. На данный момент в api
    приложения есть ошибка - приложение принимает спецсимволы в  имени питомца и не выдает ответ об ошибке"""

   # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet_no_photo(auth_key, name, animal_type, age)

    # Проверяем, что статус полученного ответа говорит о том, что предоставлены некорректные данные
    assert status == 400

# тест 4
def test_new_pet_no_negative_number_age(name='Тобик', animal_type='щеночек',
                                     age=-4, pet_photo='images/tobik.jpg'):
    """Проверяем что невозможно добавить питомца с отрицательным значением возраста.
    На данный момент в api приложения есть ошибка - приложение принимает отрицательное число в качестве значения возраста
    питомца и не выдает ответ об ошибке"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом - что статус полученного ответа говорит о том, что предоставлены некорректные данные
    assert status == 400
    assert result['age'] == age

# тест 5
def test_new_pet_no_empty_name(name='', animal_type='щеночек',
                                     age=4, pet_photo='images/tobik.jpg'):
    """Проверяем что невозможно добавить питомца с пустым именем.
    На данный момент в api приложения есть ошибка - приложение принимает пустое значение имени нового питомца
    и не выдает ответ об ошибке"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом - что статус полученного ответа говорит о том, что предоставлены некорректные данные
    assert status == 400
    assert result['name'] == name

# тест 6
def test_add_new_pet_with_invalid_photo(name='Тобик', animal_type='щеночек',
                                     age=4, pet_photo='images/not_foto.doc'):
    """Проверяем что невозможно добавить питомца с фото, если фото представлено в файле с расширением .doc.
     На данный момент в api приложения есть ошибка - приложение принимает файлы с расширением .doc для фото питомца
     и не выдает ответ об ошибке"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert result['pet_photo'] == pet_photo

# тест 7
def test_add_new_name_very_long(name='ytKSAczOvSetITskVoDRjaLmMuPeKedbHqVMvNqwjdiYXHuUHLYWIbtUfBKQRkrvNhuvdSkIOQyVWHayfTPffqBqRjmQEERQritIGyLtVedDtteNpKRGWJrkpIlITXwKQuSopevrAVsiWhaJxLTjftiVoHhtRFGVevvMnsDIDQpGjCjZhjsvTNxOxIBkeDBpBBmFSPtIQMAqhVlwTzSrcvgHouAXgxUHlGbgayXEVOcGWlPwSowQAyORrJuzFyLh', animal_type='щеночек',
                                     age=4, pet_photo='images/tobik.jpg'):
    """Проверяем что невозможно добавить питомца с количеством 256 знаков в имени.
    На данный момент в api приложения есть ошибка - приложение принимает очень длинные значения имени нового питомца (256 знаков)
    и не выдает ответ об ошибке"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом - что статус полученного ответа говорит о том, что предоставлены некорректные данные
    assert status == 400
    assert result['name'] == name

# тест 8
def test_delete_others_pet():
    """Проверяем, что невозможно удалить чужого питомца. Тест  генерирует ключ авторизации, создаетнового питомца, выводит его данные,
    получает список всех питомцев текущего пользователя; генерирует ключ авторизации друго пользователя, от его имени отправляет
    запрос на удаление питомца первого пользователя, выводит сообщение о том, есть ли питомец в списке всех питомцев первого
    пользователя, проверяет код ответа.
    На данный момент в api приложения есть ошибка - приложение позволяет удалять чужого питомца.
    и не выдает ответ об ошибке"""
    # Получаем ключ auth_key
    _, auth_key1 = pf.get_api_key(valid_email, valid_password)

    # Создаем питомца для теста с помощью метода без добавления фото, выводим сообщение о создании питомца и его данных, чтобы убедиться, что питомец был создан.
    test_pet = pf.add_new_pet_no_photo(auth_key1, 'Фунтяшка', 'поросенок', 5)
    print(f'Питомец записан. Данные питомца: {test_pet}')

    # Сохраняем в переменной id созданного тестового питомца
    pet_id = test_pet[1]['id']

    # Создаем список своих питомцев
    _, my_pets = pf.get_list_of_pets(auth_key1, "my_pets")

    # Получаем ключ auth_key2 для контрольного зарегистрированного в приложении аккаунта - email: tester123@mail.ru pass: 12345
    _, auth_key2 = pf.get_api_key('tester123@mail.ru', '12345')

    # Используя ключ контрольного акканту отправляем запрос на удаление питомца, созданного другим пользователем
    status, _ = pf.delete_pet(auth_key2, pet_id)

    # Проверяем есть ли созданный питомец в списке моих питомцев после запроса на удаление и выводим соответсвующее сообщение.
    if pet_id in my_pets.values():
        print('Питомец на месте')
    else:
        print('Питомца в списке больше нет')

    # Проверяем  статус ответа - он должен быть равен 403.
    assert status == 403

# тест 9
def test_get_api_key_for_invalid_user(email='invalidemail@mail.ru', password='123456'):
    """ Проверяем, что запрос api ключа не работает для незарегистрированного пользователя и возвращает статус 403"""

    # Отправляем запрос и сохраняем полученный ответ с кодом статуса в status, а текст ответа в result
    status, result = pf.get_api_key(email, password)

    # Сверяем полученные данные с нашими ожиданиями
    assert status == 403
    assert 'key' not in result

# тест 10
def test_unable_update_others_pet(name='Теперь этой мой питомец', animal_type='мой зверь', age=3):
    """Проверяем невозможность обновления информации о чужом питомце.
    На данный момент в api приложения есть ошибка - приложение позволяет вносить изменения в данные чужого питомца
    и не выдает ответ об ошибке"""
    # Получаем ключ auth_key
    _, auth_key1 = pf.get_api_key(valid_email, valid_password)

    # Создаем питомца для теста с помощью метода без добавления фото, выводим сообщение о создании питомца и его данных, чтобы убедиться, что питомец был создан.
    test_pet = pf.add_new_pet_no_photo(auth_key1, 'Тестовый питомец', 'поросенок', 5)
    print(f'Питомец записан. Данные питомца: {test_pet}')

    # Сохраняем в переменной id созданного тестового питомца
    pet_id = test_pet[1]['id']

    # Получаем ключ auth_key2 для контрольного зарегистрированного в приложении аккаунта - email: tester123@mail.ru pass: 12345
    _, auth_key2 = pf.get_api_key('tester123@mail.ru', '12345')

    # Используя ключ контрольного акканту отправляем запрос на внесение изменений в данные питомца, созданного другим пользователем
    status, result = pf.update_pet_info(auth_key2, pet_id, name, animal_type, age)

    # Проверяем  статус ответа - он должен быть равен 403.
    assert status == 403