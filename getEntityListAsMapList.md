# getEntityListAsMapList

---

Преобразование списка сущностей в список соответствия для их полей.
Эта функция используется преимущественно для заполнения таблиц данным сущностей.
Каждая запись в списке является 'строкой', представляющую собой сущность.
Строка данных представляет собой соответствия полных имен полей их значениям для соответствующей сущности.

#### Возвращает:

`List<Map<String, Object>>`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | entityList | Список сущностей, чаще всего получаемых из функции `GetEntities()`. | List of ECM entities |

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



[На главную](./ecmfunctions/)