#getSASStoredProcessURL

---

Возвращает URL-адрес хранимого процесса SAS, используя директиву STPRun.

#### Возвращает:

String

## Аргументы

Отсутствуют

## Примеры

**Пример 1:** В следующем примере URL возвращается для веб-приложения хранимого процесса SAS.
```xml
<action-group>
  <action>
    <param name="_action">form,properties,execute,nobanner,newwindow</param>
    <param name="_program">/Products/SAS Intelligence Platform/Samples/Sample: Stored Process Macro Variables</param>
    <param name="favoriteColor" value="'blue'"></param>
    <url>
      <eval>getSASStoredProcessURL()</eval>
    </url>
    <label>getSASStoredProcessURL testing</label>
  </action>
</action-group>
```

