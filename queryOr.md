# queryOr

---

Функция, которая возвращает CompositeSearchFilter с оператором OR **

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
QueryOr(QueryEquals(PARTY.PARTY_TYPE_CD, 'HDR'), QueryEquals(PARTY.SOURCE_SYSTEM_CD, 'SASECM'))
implies
PARTY.PARTY_TYPE_CD='HDR' OR PARTY.SOURCE_SYSTEM_CD='SASECM'.
```

**Пример 2:** Пример использования функции, которая в качестве аргумента использует Составной фильтр.
```
QueryOr(QueryEquals(INCIDENT.INCIDENT_TYPE_CD, 'GEN'), QueryOr(QueryEquals(INCIDENT.INCIDENT_CATEGORY_CD, 'EXT'), QueryEquals(INCIDENT.INCIDENT_SUBCATEGORY_CD, 'MLD')))
implies
INCIDENT.INCIDENT_TYPE_CD='GEN' OR (INCIDENT.INCIDENT_CATEGORY_CD='EXT' OR INCIDENT.INCIDENT_SUBCATEGORY_CD='MLD').
```



[На главную](./ecmfunctions/)