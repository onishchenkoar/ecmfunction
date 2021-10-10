# getFilteredLabelValues

---

Функция используется для поиска значений в справочных таблицах с универсальными данными, основанных на родительской таблице для последовательных выпадающих списков.

#### Возвращает:

`Collection<LabelValueBean>`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | tableName | Имя таблицы в справочной таблице | `String` |
| 2 | parentTableName | Имя родительской таблицы в справочной таблице | `String` |
| 3 | parentCodeValue | Значение родительского поля. | `String` |
| 4...n | activeOnly | определяет, нужно ли выполнять фильтрацию результатов для того, чтобы включать только активные значения. По умолчанию используется значение `true`. | `Boolean` |

## Примеры

****Пример 1
```xml
<field name="CASE.CASE_CATEGORY_CD"
       type="dropdown"
       readonly="true"
       values="GetFilteredLabelValues('RT_CASE_CATEGORY', 'RT_CASE_TYPE', CASE.CASE_TYPE_CD)"
>
  <label>
    <message key="field.case.case_category_cd.label.txt" />
  </label>
</field>
```



[На главную](./ecmfunctions/)