# getEFileReports

---

Возвращает список всех отчетов, которые можно добавить к объекту e-file.

#### Возвращает:

Неизвестно

## Аргументы

Отсутствуют

## Примеры

**Пример 1:** В данном примере приводится таблица со всеми отчетами, которые можно добавить к объекту e-file.
```xml
<field name="TEMP.EFILE_REPORTS" type="component" required="true" component-name="SelectableDataTable">
   <param name="rowData" value="GetEFileReports()" />
   <param name="entryKeyField" value="'RR.RR_RK'" />
   <param name="selectable" value="true" />
   <param name="selectMultiple" value="true" />
   <param name="field" value="'RR.RR_ID'" />
   <param name="field" value="'RR.SOURCE_SYSTEM_CD:RT_SOURCE_SYSTEM'" />
   <param name="field" value="'RR.RR_DESC'" />
   <param name="field" value="'RR.OWNER_USER_ID:user_name'" />
</field>
```



[На главную](./ecmfunctions/)