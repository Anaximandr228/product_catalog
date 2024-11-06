# API Продуктового каталога


## Для запуска приложения:
1. Для создания контейнера введите команду ``docker compose build``
2. Для запуска контейнера введите команду ``docker compose up``
3. Для запуска проверки линтером введите команду ``docker exec product_catalog-web-1 bash -c "poetry run flake8"``
4. Для запуска проверки тестами введите команду ``docker exec product_catalog-web-1 bash -c "poetry run pytest"``

## Для проверки эндпоинтов:
1. Вызовите "/type" и передайте в него тип продукта
2. Вызовите "/products" и передайте в него имя продукта и "product_type_id" = 1
3. Вызовите "/products" для просмотра добавленного продукта и его типа
4. Вызовите "/products/{id}" для просмотра товара по его id
5. Вызовите "/products/type/{type_id}" для просмотра товара по его типу

### CI Pipeline можно увидеть в разделе [Actions](https://github.com/Anaximandr228/product_catalog/actions)

## О проекте:
Проект разработан для получения данных о товарах и их категориях. Представлено несколько API для работы с данным приложением, предоставляющие различные функции

### Интерфейс API
<img src="https://drive.google.com/uc?export=view&id=1AiXAxGTSXw7ReGTAtjXuPSEoaq5WBrmY"><br>
<img src="https://drive.google.com/uc?export=view&id=15zh74ZnulAg-OwbIqzdtfoVNYHj5iQkM"><br>
<img src="https://drive.google.com/uc?export=view&id=1wiRJGc0ZYChPM2RI09FVhFnw597me1Lv"><br>
