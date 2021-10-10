#getReportParentSubjects

---

Возвращает субъектов, связанных с родительской сущностью отчета.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1...n | entityKeyForSubjects | указывает список ключей сущностей для поиска субъектов. | `String` |

## Примеры

**Пример 1:** Устанавливает для параметра значение, возвращенное функцией.
```xml
<param name="rowData" value="GetReportParentSubjects(GetParentGenericEntityTableKeys('X_SUSPECT.X_PARTY_RK'))" />
```

