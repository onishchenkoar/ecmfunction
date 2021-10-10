# getLabelValues

---

Возвращает упорядоченный список java.util.Collection объектов org.apache.struts.util.LabelValueBean, содержащий все активные значения для справочной таблицы.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | referenceTableName | указывает имя в справочной таблице | String |
| 2...n | activeOnly | определяет, нужно ли выполнять фильтрацию результатов для того, чтобы включать только активные
значения. По умолчанию используется значение true. | Boolean |

## Примеры

**Пример 1:** Заполнение выпадающего списка всеми значениями из справочной таблицы.
```xml
<field name="CASE.SOURCE_SYSTEM_CD" type="dropdown" readonly="true"      values="GetLabelValues('RT_SOURCE_SYSTEM')">
   <label>
      <message key="field.case.source_system_cd.label.txt" />
   </label>
</field>
```

