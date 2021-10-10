#getSecurityFilteredCategories

---

Функция выполняет поиск в списке кодов категорий сущностей, которые могут быть созданы пользователем. Используется для создания всплывающих диалоговых окон.

#### Возвращает:

`Collection<LabelValueBean>`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | entityTypeName | Имя типа сущности. | `String` |
| 2 | entityTypeCode | Текущее значения для кода типа. | `String` |

## Примеры

****Пример 1
```xml
<field name="CASE.CASE_CATEGORY_CD"
       type="dropdown"
       values="GetSecurityFilteredCategories('CASE', CASE.CASE_TYPE_CD)">
  <label>
    <message key="field.case.case_category_cd.label.txt" />
  </label>
</field>
```

