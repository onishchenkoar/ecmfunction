# getFilteredGenericDataLabelValues

---

Функция используется для поиска значений в справочных таблицах с универсальными данными, основанных на родительской таблице.
Она используется с компонентом TypeAhead.

#### Возвращает:

`Collection<LabelValueBean>`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | tableName | Имя таблицы в справочной таблице | `String` |
| 2 | valueField | Имя поля для поиска. | `String` |
| 3...n | queryFilters | Один или несколько объектов QueryFilter для поиска на основе подхода "slowly changing dimension". Более подробную информацию см. в описании функции `CreateQueryFilter` | `String` |

## Примеры

**Пример 1**
```xml
<field name="CASE.X_INSTITUTION_RK" type="dropdown" required="false"
   values="GetFilteredGenericDataLabelValues(
      'X_INSTITUTION', 'X_INSTITUTION_NM',
      CreateQueryFilter('X_INSTITUTION', 'X_INSTITUTION_OPEN_DT', '&lt;=', CASE.CREATE_DTTM),
      CreateQueryFilter('X_INSTITUTION', 'X_INSTITUTION_CLOSE_DT', '&gt;=', CASE.CREATE_DTTM)
   )">
...
</field>
```

