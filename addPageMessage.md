# addPageMessage

---

Позволяет добавлять сообщения, отображаемые для страницы, добавляемые при инициализации страницы.

#### Возвращает:

`Boolean`

Возвращает true если сообщение добавлено успешно (или если messageType = 'ignore'), или false если
возникает критическая ошибка.

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | messageKey | Ключ к локализованному сообщению в одном из файлов properties с ресурсами. | `String` |
| 2 | messageType | Одно из значений, `'status'`, `'info'`, `'warn'`, `'error'`, or `'ignore'`. Если вы укажете `'ignore'`, сообщения не будут отображаться. | `String` |
| 3 | messageArguments | Значения (от ноля и больше), переданные для замены токна в значение ключа сообщения. | `String` |

## Примеры

**Пример 1:** Добавление сообщения для первого отображения страницы.
```xml
<initialize>
   <set name="CUSTOM_DT" value="Today()" />
   <set name="TEMP.SET_PAGE_DIRTY" value="SetPageDirty()" />
   <set name="TEMP.SET_PAGE_MSG_1"
        value="AddPageMessage('some.message.key.txt', 'info')"
   />
   <set name="TEMP.SET_PAGE_MSG_2"
        value="AddPageMessage('some.message.key.fmt',
                              'info',
                              'parameter 0 of the message',
                              'parameter 1 of the message',
                              'etc.'
                             )"
   />
   <!-- Example of some.message.key.fmt in custom.properties:  -->
   <!-- some.message.key.fmt=My message: {0}, {1}, {2} -->
   <!-- Gets converted to: My message: 'parameter 0 of the message', 'parameter 1 of the message', 'etc.' -->
</initialize>
```

**Пример 2:** Отображение сообщения в зависимости от заданного условия.
```xml
<set name="TEMP.ADD_MSG_SUCCESS"
     value="AddPageMessage('some.message.key.txt', if(TEMP.ADD_MSG_FLG, 'info', 'ignore'))"
/>
```

