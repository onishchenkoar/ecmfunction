#getSASDataAsMapList

---

Эта функция вызывает хранимый процесс и загружает результаты как MapList, который используется в таблице. Результаты не добавляются в UIContext. Результаты хранимого процесса должны быть строкой xml, сгенерированной из таблицы, определенной в файле entity-prepopulate.map. Примечание: Значения даты и времени должны быть возвращены как строковое значение с датой в соответствии со стандартами ISO8601.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | stp | Полный путь и имя вызываемого хранимого процесса. | String |
| 2 | entityType | Требуется использование одного из следующих значений: 'CASE', 'INCIDENT', 'PARTY', 'RR', 'EFILE',
'FINANCIAL\_ITEM'. | String |
| 3...n | params | Ноль и более аргументов, представляющей пары значений, передаваемые в хранимый процесс | String |

## Примеры

**Пример 1:** В этом примере демонстрируется вызов функции для загрузки данных для таблицы.
```xml
<datagrid
  name="MY_LIST_GRID"
  lazy="true"
  data="GetSASDataAsMapList(
          'get_list_stored_process',
          'INCIDENT',
          'query_type=M',
          Concat('user_id=', getUserId())
        )">
  <label>My List</label>
  <datagrid-column name="INCIDENT.INCIDENT_RK">
    <label>Incident RK</label>
  </datagrid-column>
</datagrid>
```

