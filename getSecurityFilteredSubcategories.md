# getSecurityFilteredSubcategories

---

Функция выполняет поиск в списке кодов подкатегорий сущностей, которые могут быть созданы пользователем. Используется для создания всплывающих диалоговых окон.

#### Возвращает:

Collection<LabelValueBean>

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | entityTypeName | Имя типа сущности. | `String` |
| 2 | caseCategoryCode | Текущее значения для кода категории. | `String` |

## Примеры

****Пример 1
```xml
<field name="CASE.CASE_SUBCATEGORY_CD"
       type="dropdown"
       values="GetSecurityFilteredSubcategories('CASE', CASE.CASE_CATEGORY_CD)">
  <label>
    <message key="field.case.case_category_cd.label.txt" />
  </label>
</field>
```

