#  getSASNLFormattedDate

---

Форматирование даты по образцу, используемому в SAS.

#### Возвращает:

String

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | date | Указывает дату для форматирования. | `date` |
| 2 | formatName | Имя формата SAS NLFormat, применяемого к дате. | `string` |

## Примеры

**Пример 1:** Применение к дате формата 'NLDATE2'.
```xml
<set-value name="TEMP.FORMATTED_VALID_FROM_DTTM" value="GetSASNLFormattedDate(CASE.VALID_FROM_DTTM, 'NLDATE2')"/>
```



[На главную](./ecmfunctions/)

[На главную](./ecmfunctions/)