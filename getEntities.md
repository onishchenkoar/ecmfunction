# getEntities

---

Возвращает список сущностей определенного типа, которые могут удовлетворять определенному критерию.

#### Возвращает:

`List`

Список сущностей.

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | entityType | Тип сущности, которую следует извлечь. В качестве сущности следует указать `'case'`, `'incident'`, `'party'`, `'report'`, или `'efile'`. | `String` |
| 2 | keys | Необязательный список ключей извлекаемых сущностей. Если этот аргумент не используется, то возвращаются все сущности данного типа. В описании функции `getSearchKeys()` указывается как извлечь ключи для всех сущностей, которые соответствуют определенному критерию. | `List` |

## Примеры

**Пример 1:** В этом примере приводится употребление этой функции для отображения всех доступных дел в таблице.
```xml
<datagrid name='CASE.GRID' selectedKeyField='CASE.CASE_RK'>
   <datastore id='CASE.GRID.store' data='GetEntityListAsMapList(GetEntities("case"))' />
   <datagrid-column name='CASE.CASE_ID'>
      ... renderer and label ...
   </datagrid-column>
   ... other columns ...
</datagrid>
```

**Пример 2:** В этом примере приводится употребление этой функции для отображения всех доступных дел в таблице, созданных определенным пользователем.
```xml
<datagrid name='CASE.GRID' selectedKeyField='CASE.CASE_RK'>
   <datastore
     id='CASE.GRID.store' 
     data='GetEntityListAsMapList(GetEntities("case", GetSearchKeys("case", QueryEquals("CASE.CREATE_USER_ID", TEMP.SELECTED_USER))))'
   />
   <datagrid-column name='CASE.CASE_ID'>
      ... renderer and label ...
   </datagrid-column>
   ... other columns ...
</datagrid>
```

