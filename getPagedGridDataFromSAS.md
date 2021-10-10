#getPagedGridDataFromSAS

---

GetPagedGridDataFromSAS это специальная функция, которая возвращает результаты постранично, а не в полном наборе. Предлагается в качестве альтернативы функции RunSASDataLoader. Эта функция выполняет запрос хранимого процесса для того же формата документов entity-prepopulate.map. Функция GetPagedGridDataFromSAS добавляет к запросу параметры URL start, limit, sort_by, sort_dir, или любые другие дополнительные параметры. Функция также возвращает общее число записей.Параметр "sort_by" для URL это ID колонки, по которой выполняется сортировка. Если для сортировки используется несколько колонок, значением параметра будет список ID колонок, разделенных запятыми. Если сортировка не требуется, значением параметра будет пустая строка. Параметр URL "sort_dir" имеет значение "ASC" или "DESC", что означает сортировку по возрастанию или убыванию. Если сортировка выполняется по нескольким колонкам, значение параметра - список значений, разделенных запятыми. Число значений, разделенных запятыми, будет соответствовать числу значений в параметре "sort_by". Если сортировка не требуется, значением параметра будет пустая строка.

#### Возвращает:

Datagrid Data

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | STP | Хранимый процесс, который вам требуется вызвать. | String |

## Примеры

**Пример 1:** Пример запроса STP
```xml
<datastore data="GetPagedGridDataFromSAS('remote_datastore_test', 'PARTY', 'TEMP.SAS_TOTAL', concat('filter_id=', TEMP.X_ID))" id="REMOTE_STORE_SAS"/>
```
