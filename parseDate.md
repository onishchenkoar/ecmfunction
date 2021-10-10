# parseDate

---

Функция `parseDate()` возвращает парсинг даты на основе Java SimpleDateFormat.

#### Возвращает:

`Date`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | dateString | Указывает строку с датой (например, 01/01/2019). | `String` |
| 2 | datePattern | Указывает формат даты (например, MM/dd/yyyy). | `String` |

## Примеры

**Пример 1:** Оператор SET использует функцию parseDate для того, чтобы заполнить FUTURE_DATE значением даты, из dateString, парсинг которой выполняется на основе datePattern.
```xml
<set name="FUTURE_DATE" value="parseDate('01/01/2019', 'MM/dd/yyyy')"/>
```

