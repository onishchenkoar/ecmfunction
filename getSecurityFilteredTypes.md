#getSecurityFilteredTypes

---

Функция выполняет поиск в списке типов сущностей, которые могут быть созданы пользователем. Используется для создания всплывающих диалоговых окон.

#### Возвращает:

Collection<LabelValueBean>

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | entityTypeName | Имя типа сущности. | String |

## Примеры

****Пример 1
```xml
<field name="CASE.CASE_TYPE_CD" type="dropdown" values="GetSecurityFilteredTypes('CASE')"><label><message key="field.case.case_category_cd.label.txt" /></label></field>
```

