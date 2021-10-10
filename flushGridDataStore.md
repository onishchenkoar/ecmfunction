# flushGridDataStore

---

Clears the DataStore of the named DataGrid. Useful in the `<initialize>` block of a dialog screen.

#### Возвращает:

`Boolean`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | gridName | The name of the grid. | `String` |

## Примеры

**Пример 1:** Sets a parameter to the value returned by the function.
```xml
<set name="TEMP.DATA_STORE_FLUSHED" value="FlushGridDataStore('GRID_NAME')" />
```

