#getSNADirectiveURL

---

Функция, которая использует директиву для формирования URL, открывающего приложение SNA.

#### Возвращает:

String

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | partyRK | Ключ записи субъекта, используемого как начальный узел в графике SNA. | `Long` |

## Примеры

**Пример 1:** В этом примере приводится использование функции как параметра для компонента `IFrameComponent`.
```xml
<field name="TEMP.SNA_IFRAME" type="component" component-name="IFrameComponent">
   <param name="url" value="GetSNADirectiveURL(PARTY.PARTY_RK)" />
</field>
```

