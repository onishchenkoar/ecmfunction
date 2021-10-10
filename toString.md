# toString

---

Функция `toString()` преобразует объект в строку.

#### Возвращает:

`String`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | value | Указывает объект для преобразования. | `Object` |

## Примеры

**Пример 1:** Устанавливает значение по умолчанию для controlCertificationId как преобразованное строковое значение controlCertificationRk.
```xml
<field name="controlCertificationId"
       type="string"
       visible="false"
       default="toString(controlCertificationRk)">
  <label>
    <message key="controlCertification.field.controlCertificationId.displayName.txt" />
  </label>
</field>
```



[На главную](./ecmfunctions/)