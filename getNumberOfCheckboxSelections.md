# getNumberOfCheckboxSelections

---

Используется для получения числа элементов, выбранных при помощи группы флажков.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | fieldName | Имя поля, которое содержит значения флажков. | String |

## Примеры

**Пример 1:** Описание использования этой функции для получения числа элементов, выбранных при помощи группы флажков.
```xml
<validation test="GetNumberOfCheckboxSelections('X_SUSPICIOUS_ACTIVITY.X_SUSPICIOUS_ACTIVITY_CD') LT 11 ">
      <errmsg>
         <message key="field.report.summary_activity.error.txt" />
      </errmsg>
  </validation>
```

