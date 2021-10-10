# runSASDataLoader

---

Функция вызывает хранимый процесс и загружает результаты в поля в UIContext.
Результаты хранимого процесса должны храниться в строке xml, сгенерированной из таблицы, определенной в файле entity-prepopulate.map.

**Примечание**: значения Дата/время должны возвращаться как строковое значение, представляющее дату на основе стандартов ISO8601.

#### Возвращает:

`boolean`

Был ли успешным запрос STP. Вы можете выбрать этот параметр для того, чтобы отображать сообщение об ошибке в случае сбоя загрузки данных.

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | stp | Полный путь и имя вызываемого хранимого процесса. | `String` |
| 2 | entityType | Требуется использование одного из следующих значений: 'CASE', 'INCIDENT', 'PARTY', 'RR', 'EFILE', 'FINANCIAL\_ITEM'. | `String` |
| 3...n | params | Ноль и более аргументов, представляющей пары значений, передаваемые в хранимый процесс | `String` |

## Примеры

**Пример 1:** В данном примере демонстрируется вызов функции для загрузки данных в UIContext во время инициализации страницы
```xml
<initialize>
  <set name="TEMP.EXTERNAL_DATA_LOAD_FLG"
       value="runSASDataLoader('stpName', 'CASE', 'PARAM_1=XYZ', Concat('PARAM_2=', CASE.CREATE_DTTM))" />
  <if test="!TEMP.EXTERNAL_DATA_LOAD_FLG">
    <set name="TEMP.IGNORED" value="AddPageMessage('An error occurred loading data for this screen.', 'error')"/>
  </if>
</initialize>
```

