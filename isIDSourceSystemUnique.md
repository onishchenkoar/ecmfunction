# isIDSourceSystemUnique

---

Возвращает `true` если ID и код исходной системы уникальны.
Если существует другое дело, инцидент или субъект с этими же ID и кодом исходной системы, возвращает `false`.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | id | задает ID дела, инцидента или субъекта. | `String` |
| 2 | sourceSystemCode | задает код исходной системы дела, инцидента или субъекта. | `String` |

## Примеры

**Пример 1:** Проверяет уникальность ID и кода исходной системы дела.
```xml
<validation test="isIDSourceSystemUnique(CASE.CASE_ID, CASE.SOURCE_SYSTEM_CD)">
   <errmsg>
      <message key="field.id.source_system_cd.not.unique.error.fmt" />
   </errmsg>
</validation>
```



[На главную](./)