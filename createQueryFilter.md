# createQueryFilter

---

Эта функция используется для того, чтобы задать параметры поиска в следующих функциях:
* GetFilteredGenericDataLabelValues;
* GetFilteredGenericDataTypeAheadItems;
* GetFilteredGenericDataEntryValue.

#### Возвращает:

com.sas.solutions.casemgmt.cpb.function.AppQueryFilter

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | referenceTableName | указывает имя в справочной таблице | `String` |
| 2 | referenceFieldName | указывает имя поля в справочной таблице | `String` |
| 3 | operator | указывает оператор, который следует использовать с фильтром. Допустимые значения: =, <=, <, >= и >. | `String` |
| 4 | value | указывает значение, которое следует использовать для сравнения | `String` |

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



[На главную](./)