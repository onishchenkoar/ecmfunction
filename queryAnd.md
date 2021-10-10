# queryAnd

---

Функция, которая возвращает CompositeSearchFilter с оператором AND **

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | SearchFilter1 | Поиск фильтра с именем и значением/значениями | `SearchFilter` |
| 2 | SearchFilter2 | Поиск фильтра с именем и значением/значениями | `SearchFilter` |

## Примеры

**Пример 1:** Пример использования функции, которая в качестве аргумента использует Основной фильтр.
```
QueryAnd(QueryEquals(PARTY.PARTY_TYPE_CD, 'HDR'), QueryEquals(PARTY.PARTY_CATEGORY_CD, 'SCN'))
implies
PARTY.PARTY_TYPE_CD='HDR' AND PARTY.PARTY_CATEGORY_CD='SCN'.
```

**Пример 2:** Пример использования функции, которая в качестве аргумента использует Составной фильтр.
```
QueryAnd(QueryEquals(PARTY.PARTY_TYPE_CD, 'HDR'), QueryAnd(QueryNull(PARTY.PARTY_CATEGORY_CD, 'false'), QueryNull(PARTY.PARTY_SUBCATEGORY_CD, 'true')))
implies
PARTY.PARTY_TYPE_CD='HDR' AND (PARTY.PARTY_CATEGORY_CD is not null AND PARTY.PARTY_SUBCATEGORY_CD is null).
```

