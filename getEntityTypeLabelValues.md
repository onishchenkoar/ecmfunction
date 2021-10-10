# getEntityTypeLabelValues

---

Возвращает упорядоченный список `java.util.Collection` объектов `org.apache.struts.util.LabelValueBeans`,
задающий мэппинг типов сущностей (CASE, INCIDENT, PARTY, RR, EFILE) с их локализованными именами, отображаемыми в приложении.

#### Возвращает:

Неизвестно

## Аргументы

Отсутствуют

## Примеры

**Пример 1:** Заполнение выпадающего списка всеми типами сущностей.
```xml
<field name="TEMP.ENTITY_TYPE" type="dropdown" values="GetEntityTypeLabelValues()">
  <label>Entity type</label>
</field>
```

