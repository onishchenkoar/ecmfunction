# validDateTime

---

Функция `validDateTime()` проверяет валидность даты и времени.
Функция `validDateTime()` проверяет имеет ли указанная строка формат `MM/DD/YYYY HH:MM:SS` и представляет ли она
валидные день, месяц, год, час, минуту и секунду. Время имеет формат 24 часа.

#### Возвращает:

`Boolean`

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1...n | date | Указывает переменную или символьный литерал, содержащий дату и время. | `Date` |

## Примеры

**Пример 1:** В данном примере демонстрируется поле ввода, в котором пользователь указывает дату и время окончания срока действия.
Если поле не пусто, имеет формат MM/DD/YYYY HH:MM:SS, и представляет валидную дату, валидация проходит успешно.
В противном случае появляется сообщение об ошибке и пользователю необходимо исправить указанные данные.
```xml
<field name="EXPIRATION_DATE_TIME" type="string">
  <label>Enter expiration date and time:</label>
  <validation test="not empty(EXPIRATION_DATE_TIME) and validDateTime(EXPIRATION_DATE_TIME)">
    <errmsg>Expiration date/time must be in the format MM/DD/YYYY HH:MM:SS</errmsg>
  </validation>
</field>
```

