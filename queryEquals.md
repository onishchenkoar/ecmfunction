# queryEquals

---

Функция, которая преображает пару имя критерия/значение и возвращает фильтр с типом поиска EQUALS или ALL_WORDS.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | criteria | Уточненное имя поля критерия | `String` |
| 2 | value | Значение поля критерия. i.e. CUS | `String` |

## Примеры

**Пример 1:** В случае наличия только одного значения, используется фильтр поиска EQUALS.
```
QueryEquals('PARTY.PARTY_TYPE_CD', 'HDR')
implies
 PARTY.PARTY_TYPE_CD = 'HDR'
```

**Пример 2:** В случае наличия нескольких значения используется фильтр поиска ALL_WORDS.
```
QueryEquals('PARTY.PARTY_TYPE_CD', 'HDR', 'GEN')
implies
PARTY.PARTY_TYPE_CD like ('%HDR%') and PARTY.PARTY_TYPE_CD like ('%GEN%')
```



[На главную](./ecmfunctions/)