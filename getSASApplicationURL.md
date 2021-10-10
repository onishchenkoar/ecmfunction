# getSASApplicationURL

---

Функция `getSASApplicationURL()` возвращает URL для указанного имени приложения SAS (например, BI Dashboard 4.3).
Вы можете использовать эту функцию для того, чтобы сгенерировать URL к любому приложению SAS.

#### Возвращает:

`String`

Возвращает URL для указанного имени приложения SAS.

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | applicationName | Имя приложения SAS. Необходимо использовать точное написание имени приложения. Имя приложения SAS можно проверить в Диспетчере конфигурации в SAS Management Console. Имя приложения отображается в поле Имя на вкладке Общее диалогового окна Свойства соответствующего приложения. | `String` |

## Примеры

**Пример 1:** В следующем примере URL возвращается для приложения SAS с именем 'Stored Process Web App 9.2'.
```xml
<action-group>
  <action>
    <param name="_action">form,properties,execute,nobanner,newwindow</param>
    <param name="_program">/Products/SAS Intelligence Platform/Samples/Sample: Stored Process Macro Variables</param>
    <param name="favoriteColor" value="'blue'"></param>
    <url>
      <eval>getSASApplicationURL("Stored Process Web App 9.2")</eval>
    </url>
    <label>getSASApplicationURL testing</label>
  </action>
</action-group>
```



[На главную](./)