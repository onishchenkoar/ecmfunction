#createXMLTextElement

---

Returns a constructed XML text element. It ensures that the text is XML-escaped.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | tagName | specifies the name of the element. | `String` |
| 2 | text | specifies the text to be used inside of the element. | `String` |

## Примеры

**Пример 1:** Sending request with XML payload to a remote service.
```
C_XMLElement( 'incidentRk', INCIDENT.INCIDENT_RK )
```

