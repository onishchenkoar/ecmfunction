#queryIn

---

Функция, которая преобразует пару имя критерия/значение и возвращает фильтр поиска с типом ANY_WORDS или EQUALS.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | criteria | Составное имя поля критерия. напр. PARTY.PARTY\_TYPE\_CD | `String` |
| 2 | value1 | Значение поля критерия, напр. CUS | `String` |
| 3 | value2 | Значение поля критерия, напр. GEN | `String` |

## Примеры

**Пример 1:** В случае наличия только одного значения, используется фильтр поиска EQUALS.
```
QueryIn('PARTY.PARTY_TYPE_CD', 'HDR')
implies
 PARTY.PARTY_TYPE_CD = 'HDR'
```

**Пример 2:** В случае наличия нескольких значения используется фильтр поиска ANY_WORDS.
```
QueryIn(PARTY.PARTY_TYPE_CD, 'HDR', 'GEN')
implies
PARTY.PARTY_TYPE_CD like ('%HDR%') or PARTY.PARTY_TYPE_CD like ('%GEN%')
```

