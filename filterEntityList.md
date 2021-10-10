# filterEntityList

---

Фильтрация списка элементов по определенному критерию.
Обратите внимание, что применение этой функции для фильтрации большого числа сущностей малоэффективно и в этих случаях
следует использовать функцию `GetEntities()` в комбинации с функцией `GetSearchKeys()`.

#### Возвращает:

`List`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | entityList | Список сущностей, которые нужно отфильтровать. | `String` |
| 2 | filterExpression | Выражение для фильтра, применяемого к списку сущностей. Пользователь может указать один или несколько фильтров.  Поля для каждой фильтруемой сущности указываются стандартным способом (т. е. `CASE.CASE_TYPE_CD`); поля со страницы следует указывать, используя префикс `'PARENT.'` (т. е. `PARENT.TEMP.REQUIRED_CASE_TYPE`). Если для какой-либо сущности из списка сущностей в выражении для фильтра возвращается значение false, то эта сущность будет удалена из списка результатов. | `String` |

## Примеры

**Пример 1:** В данном примере приводится отфильтрованый список дел. Обратите внимание, что в этом примере используется не самый эффективный способ фильтрации.
```xml
<datagrid name='CASE.GRID' selectedKeyField='CASE.CASE_RK'>
   <datastore id="CASE.GRID.store"
              data="GetEntityListAsMapList(FilterEntityList(
                      GetEntities('case'),
                      &quot;CASE.CASE_TYPE_CD='FIN'
                            and CASE.INVESTIGATOR_USER_ID=GetUserId()
                            and CASE.PRIORITY_CD=PARENT.TEMP.REQUIRED_PRIORITY&quot;
                    ))"
   />
   <datagrid-column name='CASE.CASE_ID'>
     <label>Case ID</label>
   </datagrid-column>
   ... other columns ...
</datagrid>
```

