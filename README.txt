Тестовый фреймворк для тестирования приложения test-vehicle-api.

Убедитесь что установили все зависимости из файла requirements.ini перед запуском.

test-vehicle-api работает в локальном docker.
Для тестирования в серверном режиме, необходимо добавить настройки в файл ConfFirst.py

---------------------------------------------

Запуск всех тестов
py -m pytest -v

Запуск тестов по категориям с подробным логом
py -m pytest -v -m GearPositionNeutral -vv

Запуск тестов с формированием Allure отчёта. Если в Chrome не откроется, можно открыть в FireFox или Edge
py -m pytest -vv --alluredir=allure-results
allure serve allure-results
