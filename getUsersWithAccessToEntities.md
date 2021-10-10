#getUsersWithAccessToEntities

---

Возвращает список всех пользователей, которые имеют доступ ко всем сущностям в списке.
Если такие пользователи отсутствуют, возвращается пустой список.

#### Возвращает:

`List<LabelValueBean>`

Список объектов (beans), репрезентирующих пары ID пользователя/отображаемое имя пользователя

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | entityType | Тип сущности. В качестве сущности следует указать `'case'`, `'incident'`, `'party'`, `'report'`, или `'efile'`. | `String` |
| 2 | keys | Список ключей сущностей указанного типа (например, из функции `GetSelectedRowKeys()`), или ключ одной сущности. | `List` or `Number` |

## Примеры

**Пример 1:** В этом примере демонстрируется использование функции с применением on-select к таблице данных (DataGrid)
для обновления всех пользователей, которые имеют доступ ко всем выделенным делам в таблице данных.
```xml
<datagrid name='CASE.GRID' selectedKeyField='CASE.CASE_RK'>
   <datastore id='CASE.GRID.store' data='GetEntityListAsMapList(C_GetSpecificCases())' />
   <datagrid-column name='CASE.CASE_ID'>
     ... renderer and label ...
   </datagrid-column>
     ... other columns ...
   <on-select>
     <set-values name='TEMP.USERS_DROPDOWN' values="GetUsersWithAccessToEntities('incident', GetSelectedRowKeys('CASE.GRID'))"/>
   </on-select>
</datagrid>
```

**Пример 2:** В этом примере демонстрируется использование этой функции для получения всех пользователей с доступом к одному делу.
```xml
<field name="TEMP.USERID.2" type="dropdown" values="sortLabels(GetUsersWithAccessToEntities('case', 10003))">
   <label>GetUsersWithAccessToEntities, sorted</label>
</field>
```

