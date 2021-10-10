# createJSONArrayProperty

---

Returns a constructed JSON Array Object property (such as "keys" : [ 1, 2, 3]).
It ensures that the values are escaped for JSON.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | propertyName | specifies the name of the JSON property. | `String` |
| 2 | propertyValues | array or collection of values for the JSON array. | `Object[]` or `Collection` |
| 3 | valueType | specifies the type of the array values. Numerics will not be quoted. Default is "String". | `String` |

## Примеры

**Пример 1:** Sending request with JSON payload to a remote service.
```
C_JSONArray( 'keys', GetSelectedRowKeys('MY_ALERTS_GRID') )
```



[На главную](./)