# getParentGenericEntityTableKeys

---

Возвращает родительский ключ для указанного поля.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | keyField | указывает имя поля, содержащего данные ключа. | String |

## Примеры

**Пример 1:** Возвращает ключи родительских субъектов, которые используются как параметры для другой функции.
```xml
<param name="rowData" value="GetReportParentSubjects(GetParentGenericEntityTableKeys('X_SUSPECT.X_PARTY_RK'))" />
```



[На главную](./ecmfunctions/)