#containsAnyCharIn

---

Возвращает значение, указывающее, содержится ли в строке один или несколько символов из другой строки.

#### Возвращает:

`Boolean`

Были ли найдены в строке какие-либо из символов из charStr.

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | key | Строка для поиска символов. | `String` |
| 2 | charStr | Набор символов для поиска. | `String` |

## Примеры

**Пример 1:** Возвращает ошибку, если поле содержит символ '-' или '/'.
```xml
<validation test="!containsAnyCharIn(X_SUSPECT.X_NATIONAL_ID, '-/')">
  <errmsg>
    <message key="field.x_suspect.x_national_id.error.txt" />
  </errmsg>
</validation>
```

