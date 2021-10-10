# getSelectedRowKeys

---

Возвращает список ключей для всех выбранных строк в DataGrid.
Если не выбрано ни одной строки, возвращается пустой список.
Если вы используете объект DataGrid, который поддерживает выбор только одной строки (напр. без колонок с флажком),
вы можете использовать функцию `GetSelectedDataGridItem()` для того, чтобы вернуть значение колонки из выбранной строки.

#### Возвращает:

`List`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | gridName | Имя таблицы данных | `String` |

## Примеры

**Пример 1:** В этом примере демонстрируется использование функции с применением on-select к таблице данных (DataGrid),
для обновления всех пользователей, которые имеют доступ ко всем выделенным делам в таблице данных.
```xml
<datagrid name='CASE.GRID' selectedKeyField='CASE.CASE_RK'>
   <datastore id='CASE.GRID.store' data='GetEntityListAsMapList(C_GetSpecificCases())' />
   <datagrid-column name='CASE.CASE_ID'>
     ... renderer and label ...
   </datagrid-column>
     ... other columns ...
   <on-select>
      <set-values name='TEMP.USERS_DROPDOWN' values="GetUsersWithAccessTo('incident', GetSelectedRowKeys('CASE.GRID'))"/>
   </on-select>
</datagrid>
```



[На главную](./)