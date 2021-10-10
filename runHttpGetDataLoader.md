# runHttpGetDataLoader

---

Эта функция выполняет запрос HTTP GET и загружает результаты в поля в UIContext.
Результаты запроса HTTP POST должны быть строкой xml, сгенерированной файлом entity-prepopulate.map.

**Примечание**: Значения дата/время должны быть возвращены как строковое значение, представляющее дату на основе стандартов ISO8601.

#### Возвращает:

`Boolean`

Функция вернет значение `true`, если запрос был успешным, или `false` если при выполнении запроса HTTP GET произошла ошибка.

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | url | Полный URL для вызова. | `String` |
| 2 | entityType | Требуется использование одного из следующих значений: 'CASE', 'INCIDENT', 'PARTY', 'RR', 'EFILE', 'FINANCIAL\_ITEM'. | `String` |
| 3...n | params | Ноль и более аргументов, представляющих пары значений, которые добавляются в URL. | `String` |

## Примеры

**Пример 1:** В данном примере демонстрируется вызов функции для загрузки данных в UIContext во время инициализации страницы
```xml
<initialize>
  <set name="TEMP.EXTERNAL_DATA_LOAD_FLG"
       value="runHttpGetDataLoader('http://webserver:port/webapp/services/data.xml',
                                   'CASE',
                                   'PARAM_1=XYZ',
                                   Concat('PARAM_2=', CASE.CREATE_DTTM)
                                  )" />
</initialize>
```

