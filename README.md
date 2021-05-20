Данная программа представляет собой веб-сервис на базе django, способный принимать в POST запросе .csv файл "deals.csv", и возвращает в GET запросе обработанные данные.

.csv файл должен находиться в /gems/src и содержать следующие поля:
customer - логин покупателя
item - наименование товара
total - сумма сделки
quantity - количество товара, шт
date - дата и время регистрации сделки

Обработанные данные представляют собой список из 5 наиболее потратившихся клиентов, сумму потраченную ими за все время, и список из названий камней, которые 
купили как минимум двое из списка "5 клиентов, потративших наибольшую сумму за весь период", и данный клиент является одним из этих покупателей.

Приложение контейнеризовано в docker, команда для запуска - "docker-compose up"
