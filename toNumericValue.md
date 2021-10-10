# toNumericValue

---

Функция `toNumericValue()` преобразует объект в число.

#### Возвращает:

`Double`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | value | Указывает объект для преобразования. | `Object` |

## Примеры

**Пример 1:** Вычисление суммы двух параметров именованного списка с числовыми значениями
```xml
<field name="TEMP.FIELD1" type="dropdown" values="GetNamedListLabelValues('x_sample')" >
  <label>Field 1</label>
  <on-change>
    <set-value name="TEMP.FIELD3" value="ToNumericValue(TEMP.FIELD1) + ToNumericValue(TEMP.FIELD2)" />
  </on-change>
</field>
<field name="TEMP.FIELD2" type="dropdown" values="GetNamedListLabelValues('x_sample')" >
  <label>Field 2</label>
  <on-change>
    <set-value name="TEMP.FIELD3" value="ToNumericValue(TEMP.FIELD1) + ToNumericValue(TEMP.FIELD2)" />
  </on-change>
</field>
<field name="TEMP.FIELD3" type="readonly" >
  <label>Sum of field 1 and 2</label>
</field>
```

