#getStoredProcessProgramPath

---

Функция, которая используется для получения пути к коду хранимого процесса приложения. Он хранится в метаданных в файлах property, STP.Source.Path

#### Возвращает:

Неизвестно

## Аргументы

Отсутствуют

## Примеры

**Пример 1:** Устанавливает для параметра значение отформатированного свойства.
```xml
<action-group>
   <action url="GetSASStoredProcessURL()" output-destination="inline" content-type="application/x-form-url-encoded">
      <label><message key="efile.generate.action.label.txt"/></label>
      <param name="_action" value="'execute,nobanner'" />
      <!-- Path to the stored process to execute -->
      <param name="_program"            value="Concat(GetStoredProcessProgramPath(), '/ecmrr_efile')" />
      <!-- You can put in a field name here -->
      <param name="efile_rk" value="EFILE.EFILE_RK" />
   </action>
</action-group>
```

