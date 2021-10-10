# queryNull

---

Возвращает фильтр, который выполняет поиск исходя из того, является ли определенное поле пустым (`null`) или не пустым (non-null).
`QueryNull('PARTY.PARTY_CATEGORY_CD', true)` предполагает `PARTY.PARTY_CATEGORY_CD IS NULL`.
`QueryNull('PARTY.PARTY_CATEGORY_CD', false)` предполагает `PARTY.PARTY_CATEGORY_CD IS NOT NULL`.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | criteria | Уточненное имя поля критерия | `String` |
| 2 | nullFlag | Идентифицирует ли фильтр записи, в которых это поле пустое (null) или не пустое (non-null). Этот параметр не обязателен и если он не указан, по умолчанию используется значение true. | `boolean` |

## Примеры

**Пример 1:** Пример использования IS_NULL. Возвращается тип фильтра IS_NULL.
```
QueryNull('PARTY.PARTY_CATEGORY_CD', true)
implies
PARTY.PARTY_CATEGORY_CD IS NULL
```

**Пример 2:** Пример использования NOT_NULL. Возвращается тип фильтра NOT_NULL.
```
QueryNull('PARTY.PARTY_CATEGORY_CD', false)
implies
PARTY.PARTY_CATEGORY_CD IS NOT NULL
```



[На главную](./)