# getFilteredGenericDataTypeAheadItems

---

Функция используется для поиска значений в справочных таблицах с универсальными данными, основанных на родительской таблице. Она используется с компонентом TypeAhead.

#### Возвращает:

String

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | tableName | Имя таблицы в справочной таблице | `String` |
| 2 | valueField | Имя поля для поиска. | `String` |
| 3 | typeAheadField | Поле на странице, в которое будет записан ярлык возвращенного объекта. | `String` |
| 4 | keyField | Поле на странице, в которое будет записан ключ возвращенного объекта. | `String` |
| 5...n | queryFilters | Один или несколько объектов QueryFilter для поиска на основе подхода "slowly changing dimension". Более подробную информацию см. в описании функции CreateQueryFilter | `String` |

## Примеры

**Пример 1**
```xml
<field name="CASE.X_BRANCH_ID"
       type="component"
       required="false"
       component-name="TypeAhead"
>
  <label>
    <message key="field.case.x_branch_id.label.txt" />
  </label>
  <param name="items">
    GetFilteredGenericDataTypeAheadItems(
      'X_BRANCH',
      'X_BRANCH_ID',
      'CASE.X_BRANCH_ID',
      'CASE.X_BRANCH_RK',
      CreateQueryFilter(
        'X_BRANCH',
        'X_BRANCH_OPEN_DT',
        '&lt;=',
        CASE.CREATE_DTTM
      ),
      CreateQueryFilter(
        'X_BRANCH',
        'X_BRANCH_CLOSE_DT',
        '&gt;=',
        CASE.CREATE_DTTM
      )
    )
  </param>
</field>
```



[На главную](./ecmfunctions/)