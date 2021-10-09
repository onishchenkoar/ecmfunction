#getFilteredGenericDataEntryValue

---

Эта функция используется для доступа к специальным справочным таблицам с универсальными данными. Функция возвращает значение определенной колонки.

#### Возвращает:

`com.sas.solutions.casemgmt.domain.GenericDataEntry`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | tableName | Имя таблицы в справочной таблице | `String` |
| 2 | valueField | Имя поля для поиска. | `String` |
| 3...n | queryFilters | Один или несколько объектов QueryFilter для поиска на основе подхода "slowly changing dimension". Более подробную информацию см. в описании функции `CreateQueryFilter` | `String` |

## Примеры

**Пример 1:** В примере демонстрируется получение ключа rk из справочной таблицы X_BRANCH и установка его в поле отчета
RR.X_BRANCH_RK.

Примечание: в этом примере 'ENTRY_KEY' это специальное поле, которое имеет заданное соответствие с первичным ключом филиала в справочной таблице.
```xml
<set-value
  name="RR.X_BRANCH_RK"
  value="GetFilteredGenericDataEntryValue('X_BRANCH', 'ENTRY_KEY',
    CreateQueryFilter('X_BRANCH', 'X_BRANCH_ID', '=', RR.X_BRANCH_ID),
    CreateQueryFilter('X_BRANCH', 'X_BRANCH_OPEN_DT', '&lt;=', RR.PARENT_CREATE_DTTM),
    CreateQueryFilter('X_BRANCH', 'X_BRANCH_CLOSE_DT', '&gt;=', RR.PARENT_CREATE_DTTM)
  )" />
```

