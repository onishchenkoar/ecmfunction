# createJSONProperty

---

Returns a constructed JSON property (such as "empName" : "John Smith"). It ensures that the value is escaped for JSON.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | propertyName | specifies the name of the JSON property. | `String` |
| 2 | propertyValue | specifies the value to be used for the JSON property. | `Object` |
| 3 | valueType | specifies the type of the value. Numerics will not be quoted. Default is "String". | `String` |

## Примеры

**Пример 1:** Sending request with JSON payload to a remote service.
```
C_JSONProperty( 'ownerUserLongId', TEMP.USERID )
```



[На главную](./)