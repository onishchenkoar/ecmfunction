# getLocalizedDateString

---

Функция getLocalizedDateString() возвращает указанную строку в виде строки, форматированную в соответствии языковыми настройками клиента.

#### Возвращает:

String
Дата в локали клиента.

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | date | Указывает дату для форматирования. | Date |

## Примеры

**Пример 1:** Функция возвращает дату, форматированную для языковых настроек клиентского приложения, затем передает это значение как сообщение об ошибке.
```xml
<errmsg>
<message key="iap.issue.error.dateBeforeActionPlanDate.fmt.txt">
<param value="getLocalizedDateString(getLatestActionPlanTargetDt())"/>
</message>
</errmsg>
```



[На главную](./ecmfunctions/)