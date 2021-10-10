#setFieldValue

---

Sets the value of a filed. Returns `true` if the new value is different from the existing value, `false` otherwise.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | fieldName | specifies the name of the field. | `String` |
| 2 | value | specifies the value for the field. Could be a String, ArrayList or null | `String` |

## Примеры

**Пример 1:** Populating a table column with values from a reference table.
```xml
<call if="!TEMP.INIT_FLG"
      function="SetFieldValue('X_ITEM_LIST.ITEM_NAME',
                GetValueList('RT_ITEM_LIST'))"/>
```

