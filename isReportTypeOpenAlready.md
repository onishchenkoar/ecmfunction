#isReportTypeOpenAlready

---

Возвращает значение `true` если отчет переданного типа уже открыт для указанной сущности, в противном случае возвращает `false`.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | type\_cd | указывает имя разрешения, заданного в репозитории метаданных SAS. | `String` |
| 2 | category\_cd | указывает имя разрешения, заданного в репозитории метаданных SAS. | `String` |
| 3 | subcategory\_cd | указывает имя разрешения, заданного в репозитории метаданных SAS. | `String` |

## Примеры

**Пример 1:** Устанавливает для параметра значение, возвращенное функцией.
```xml
<validation test='!IsReportTypeOpenAlready(RR.RR_TYPE_CD, RR.RR_CATEGORY_CD, RR.RR_SUBCATEGORY_CD)'>
  <errmsg>
    <message key='report.multiple_reports_not_allowed.txt' />
  </errmsg>
</validation>
```

