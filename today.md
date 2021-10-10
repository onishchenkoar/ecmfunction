# today

---

Функция `today()` возвращает текущую дату.

#### Возвращает:

`Date`

## Аргументы

Отсутствуют

## Примеры

**Пример 1:** Ограничивает поле даты выбором только текущей даты.
```xml
<field name="targetDt" type="date" required="true" minSelectableDate="today()" maxSelectableDate="issue.targetDt">
  <label>
    <message key="actionPlanEx.field.targetDt.displayName.txt" />
  </label>
</field>
```



[На главную](./)