# escapeForJavaScript

---

Функция `EscapeForJavaScript` экранирует строковое значение так, чтобы его можно было включить в строку JavaScript,
встроенную в документ HTML.

#### Возвращает:

`String`

Экранированная строка для JavaScript.

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | text | Строковое значение, которое нужно экранировать. | `String` |

## Примеры

**Пример 1:** Эта функция возвращает строковое значение, которое может содержаться в строке JavaScript,
встраиваемой в документ HTML.
```xml
<datagrid-renderer id="C_mapit">
  var map = '<eval>EscapeForJavaScript(GetProperty("field.fcf.map.action.label.fmt"))</eval>';
  <![CDATA[
    var rows = arguments[1];
    return "<a target='_blank'
               href='http://maps.google.com/maps?f=q&source=s_q&q='
                    + rows["TEMP.X_RELATED_ADDRESSES_STREET"] + ","
                    + rows["TEMP.X_RELATED_ADDRESSES_CITY"] + ","
                    + rows["TEMP.X_RELATED_ADDRESSES_STATE"] + ","
                    + rows["TEMP.X_RELATED_ADDRESSES_POSTAL"]
                    + map
            </a>";
  ]]>
</datagrid-renderer>
```



[На главную](./)