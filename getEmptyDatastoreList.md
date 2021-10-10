# getEmptyDatastoreList

---

Creates an empty ListMap for use in cases when needing to initialize a datastore to an empty value.

#### Возвращает:

Неизвестно

## Аргументы

Отсутствуют

## Примеры

**Пример 1:** create an empty List Map to initialize a datastore.
```xml
<set name="TEMP.AA_ALERTS_EXPRESSION" value="'C_GetEmptyDatastoreList()'"/>
<datastore data="C_EVAL(TEMP.AA_ALERTS_EXPRESSION)" id="all_alerts_store"/>
```

