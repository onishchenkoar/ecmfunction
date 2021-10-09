#toDouble

---

Преобразует строку или число в значение Double. Если число имеет значение null или строка пустая, возвращается значение null.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | value | Число или строкa для преобразования в значение Double | Number or String |

## Примеры

**Пример 1:** В этом примере демонстрируется вызов функции для преобразование строки в значение Double.
```xml
<field name="TEMP.CHAR_VALUE" type="dropdown"
        values="GetLabelValues('RT_CHAR_NUMBERS')">
  <on-change>
     <set-value name="INCIDENT.X_DOUBLE_VALUE" value="toDouble(TEMP.CHAR_VALUE)"/>
  </on-change>
</field>
```

