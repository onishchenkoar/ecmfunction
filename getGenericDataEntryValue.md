#getGenericDataEntryValue

---

Функция, которая используется для получения значения для справочной таблицы, определенного в таблицах универсальных данных.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | tableName | Имя таблицы в справочной таблице | String |
| 2 | valueField | Имя поля для поиска. | String |
| 3 | key | Ключ поля для поиска. | String |

## Примеры

**Пример 1:** В данном примере демонстрируется установка поля Имя учреждения для дела с помощью вызова set-value в событии on-change.
```xml
<set-value
  name="CASE.X_INSTITUTION_NM"
  value="If(TEMP.IGNORE_INSTITUTION_OVERRIDE_ONCHANGE,
            CASE.X_INSTITUTION_NM,
            GetGenericDataEntryValue('X_INSTITUTION',
                                     'X_INSTITUTION_NM',
                                     CASE.X_INSTITUTION_RK
                                    )
           )"
/>)
```

