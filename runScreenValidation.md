# runScreenValidation

---

Эта функция выполняет все задачи валидации, указанные как часть в определении для UI. Функция рекурсивно проходит по всем задачам валидации в подокне определения.

#### Возвращает:

Неизвестно

## Аргументы

Отсутствуют

## Примеры

**Пример 1:** Этот пример используется определением rr-fincen-sar-01.xml UI.
```xml
<field name="TEMP.REPORT_VALIDATE" type="component" component-name="ButtonComponent">
   <label>
      <message key="rr.validate.report.txt"/>
   </label>
   <on-select>
      <call function="RunScreenValidation()" if="!TEMP.IGNORE_REPORT_VALIDATE_BUTTON"/>
      <set-value name="TEMP.IGNORE_REPORT_VALIDATE_BUTTON" value="false"/>
   </on-select>
</field>
```

