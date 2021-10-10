# getObjectTypeId

---

Возвращает ID целочисленного объекта для указанного типа сущности.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | entityType | Имя типа сущности: дело, инцидент, субъект, отчет, e-файл. | String |

## Примеры

**Пример 1:** Передает ID типа объекта текущему компоненту
```xml
<field name="comments" type="component" required="false"
        component-name="CommentsAndAttachments">
   <param name="object_type_id"
          value="GetObjectTypeId('INCIDENT')"/>
   ...
</field>
```



[На главную](./ecmfunctions/)