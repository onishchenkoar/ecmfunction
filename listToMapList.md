# listToMapList

---

Преобразавывает `List<Object>` в `List<Map<String, Object>>`. Значение "key" в каждой карте указывается вторым параметром.
Эту функцию удобно использовать с простыми таблицами, в которых отображается только одно поле (напр. для использования в качестве списка).

#### Возвращает:

`List<Map<String, Object>>`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | list | Список объектов. | A list of objects |
| 2 | fieldName | Имя поля/колонки для данных в списке. | `string` |

## Примеры

**Пример 1:** В этом примере показывается использование этой функции для заполнения DataGrid.
```xml
<datagrid name='EXAMPLE.GRID' selectedKeyField='TEMP.KEY_FIELD'>
   <datastore id="EXAMPLE.GRID.store" data="ListToMapList(C_GetListData(), 'TEMP.KEY_FIELD')" />
   <datagrid-column name='TEMP.KEY_FIELD'>
      ... renderer and label ...
   </datagrid-column>
</datagrid>
```



[На главную](./)