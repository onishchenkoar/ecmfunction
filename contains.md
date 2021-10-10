# contains

---

Функция `contains()` используется для того, чтобы определить, содержит ли список или массив указанное значение.

#### Возвращает:

`Boolean`

Возвращает значение `true` если набор содержит указанное значение.

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | collection | Указывает переменную, содержащую массив или список значений. | `Collection` |
| 2 | value | Указывает имя переменной или строковый литерал для поиска. | `Object` |

## Примеры

**Пример 1:** Сначала функция getNamedListLabelValues() возвращает набор ярлыков, которые сохраняются в TEMP.myList. Если у именованного списка 'MyNamedList' есть значение 'Red', то TEMP.containsRed будет иметь значение true.
```xml
<set name="TEMP.myList" value="getNamedListLabelValues('MyNamedList')"/>
<set name="TEMP.containsRed" value="contains(TEMP.myList, 'Red')"/>
```

