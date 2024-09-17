# Тестовое задание


## Для запуска приложения:
1. Для создания контейнера введите команду ``docker compose build``
2. Для запуска контейнера введите команду ``docker compose up``
3. Для запуска проверки линтером введите команду ``docker exec zit_test_app-web-1 bash -c "poetry run flake8"``
4. Для запуска проверки тестами введите команду ``docker exec zit_test_app-web-1 bash -c "poetry run pytest"``

## Для проверки эндпоинтов:
1. Вызовите "/type" и передайте в него тип продукта
2. Вызовите "/products" и передайте в него имя продукта и "product_type_id" = 1
3. Вызовите "/products" для просмотра добавленного продукта и его типа
4. Вызовите "/products/{id}" для просмотра товара по его id
5. Вызовите "/products/type/{type_id}" для просмотра товара по его типу
### CI Pipeline можно увидеть в разделе [Actions](https://github.com/Anaximandr228/ZIT_test_app/actions)
