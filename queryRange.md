#queryRange

---

Функция, которая возвращает фильтр поиска с типом FROM_TO.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | criteria | Составное имя поля критерия в формате PARTY.VERSION\_NO | `String` |
| 2 | from\_value | Нижний диапазон поля критерия. | `String` |
| 3 | to\_value | Верхний диапазон поля критерия. | `String` |

## Примеры

**Пример 1:** Пример со значениями from и to.
```
QueryRange('PARTY.VERSION_NO', '10', '50')
implies
PARTY.VERSION_NO >= 10 AND PARTY.VERSION_NO <= 50
```

**Пример 2:** Пример только со значением to.
```
QueryRange('PARTY.VERSION_NO', '10', '')
implies
PARTY.VERSION_NO >= 10
```

**Пример 3:** Пример только со значением from.
```
QueryRange('PARTY.VERSION_NO', '', '50')
implies
PARTY.VERSION_NO <= 50
```

