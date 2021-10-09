#queryLike

---

Функция, которая преобразует пару имя критерия/значение и возвращает фильтр поиска с типом ANY_WORDS или ALL_WORDS, что дает выражение WHERE с оператором LIKE.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | criteria | Составное имя поля критерия. напр. PARTY.PARTY\_TYPE\_CD | String |
| 2 | value1 | Значение поля критерия, напр. GEN | String |

## Примеры

**Пример 1:** Пример использования функции QueryLike с одним аргументом. Возвращается фильтр поиска типа ALL_WORDS.
```
QueryLike('PARTY.PARTY_TYPE_CD', 'GEN')
implies
PARTY.PARTY_TYPE_CD like ('%GEN%')
```

**Пример 2:** Пример использования функции QueryLike с одним аргументом с пробелами. Возвращается фильтр поиска типа ALL_WORDS.
```
QueryLike('PARTY.PARTY_FULL_NM', 'Billy Bob')
implies
PARTY.PARTY_FULL_NM like ('%Billy%') and PARTY.PARTY_FULL_NM like ('%Bob%')
```

**Пример 3:** Пример использования функции QueryLike с несколькими аргументами. Возвращается фильтр поиска типа ALL_WORDS.
```
QueryLike('PARTY.PARTY_TYPE_CD', 'HDR', 'GEN')
implies
PARTY.PARTY_TYPE_CD like ('%HDR%') or PARTY.PARTY_TYPE_CD like ('%GEN%')
```

