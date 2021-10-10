# getEntityKeysForGrid

---

This function returns the key column values for the following types of grids:
* CasePartiesGrid;
* IncidentPartiesGrid;
* LinkedPartiesGrid;
* CaseIncidentsGrid;
* EFileReportsGrid;
* LinkedCasesGrid;
* PartyEntitiesGrid;
* ReportsGrid.

#### Возвращает:

`List`

Returns list of the values for the rows of the specified keyFieldName column

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | gridName | The unique name of the grid to get the row count for. | `String` |
| 2 | keyFieldName | The name of the key field from the grid; those column values will be returned. | `String` |



[На главную](./)