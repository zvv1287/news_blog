Проект по созданию новостного блога на Django 2.2.7

Перед запуском сервера установите необходимые для работы пакеты выполнив команду
pip install -r req.txt
Примените миграции
./manage.py migrate

Для использования тестовой(моей) базы данных выполните
./manage.py loaddata db.json

Для запуска локального сервера выполните 
./manage.py runserver


Для тестирования созданны три пользователя:
varin пароль 12345
ivan пароль abracadabra1234
sidor пароль abracadabra1234

В категориях реализовано иерархическое древо. В категории спорт есть дочернии категории.
В админке при создании категории можно задать кол-во постов категории на одной странице. 
При отображении всех новостей или новостей по тегам на странице отображается 6 постов.
Также есть возможность указать используемый для категории или новости шаблон.
Для примера в категории и новостях спорта использован свой шаблон, отличающийся заголовком красного цвета.

Есть возможность создания страниц в админке по созданному заранее шаблону. 
Созданны 3 таких страницы по двум шаблонам: Главная, Шаблон 1, Шаблон 2

Меню в панели навигаии создается из админки путем добавления и удаления пунктов меню на существующий у нас объект.
Указывается сам обьект (категория, новость, страница) и его id

Из файла settings локальные настройки вынесены в отдельный файл. В продакшен они не выкладываются.
При наличии файла local_settings данные беруться из него, про его отсутствии из prod_settings



