# getCaseParties

---

Возвращает список объектов для субъектов, связанных с делом, используемый как выпадающий список для выбора параметров.
LabelValueBean это ярлык для субъекта (полное имя, если указано, если не указано, то номер паспорта, если не указан,
то ID субъекта), в качестве значения используется ключ субъекта, возвращаемый как строка.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | casePartiesFieldName | Имя компонента CasePartiesGrid. Возвращаемые значения только указывают какие данные отображаются в данной таблице, поэтому если к ней применены фильтры, то отфильтрованы будут и результаты функции. Если для этого аргумента передается null, то запрос выполняется для всех связанных с делом клиентов (что равнозначно передаче имени CasePartiesGrid без примененных фильтров). Вы можете передать `null` если текущая страница не содержит компонента CasePartiesGrid, но вам требуется доступ к связанным клиентам. | `String` |
| 2 | zeroOrMoreRelationshipTypeCodes | Указывает список соответствующих типов связей (необязательно). Если не передается кодов для типов, отображаются все клиенты, связанные с делом. | `String` |

## Примеры

**Пример 1:** В этом примере выпадающее меню содержит всех клиентов в CasePartiesGrid.
```xml
<datagrid name="parties.grid" selectedKeyField="PARTY.PARTY_RK"
          component-name="CasePartiesGrid">
  <datagrid-column name="PARTY.PARTY_ID">
    <label>Subject ID</label>
    <datagrid-renderer-ref id="sas_entityLinkRenderer" args="Party:PARTY.PARTY_RK"/>
  </datagrid-column>
  <datagrid-column name="PARTY.PARTY_FULL_NM">
    <label>Name</label>
  </datagrid-column>
  <datagrid-column name="PARTY.PARTY_TYPE_CD">
    <label>Type</label>
    <datagrid-renderer-ref id="sas_refTableRenderer" args="RT_PARTY_TYPE"/>
    <datagrid-column-sorter name="refTableSorter">
      <param name="referenceTable" value="'RT_PARTY_TYPE'" />
    </datagrid-column-sorter>
  </datagrid-column>
  <datagrid-column name="TEMP.PARTY.RELATIONSHIP">
    <label>Relationship</label>
    <datagrid-renderer-ref id="sas_refTableRenderer" args="X_RT_RELATION_TYPE"/>
    <datagrid-column-sorter name="refTableSorter">
      <param name="referenceTable" value="'X_RT_RELATION_TYPE'" />
    </datagrid-column-sorter>
  </datagrid-column>
  <datagrid-column name="TEMP.PARTY.RELATIONSHIP.DESCRIPTION">
    <label>Description</label>
  </datagrid-column>
  <datagrid-column name="PARTY.CREATE_DTTM">
    <label>Date Created</label>
    <datagrid-renderer-ref id="sas_dateTimeRenderer"/>
  </datagrid-column>
  
  <param name="relationshipTypeTable" value="'X_RT_RELATION_TYPE'"/>
  
  <on-change>
    <set-values name="TEMP.CASE_PARTIES_DROPDOWN" values="getCaseParties('parties.grid')"/>
    <!-- The line below will do the same thing, since this is an unfiltered grid. -->
    <!--set-values name="TEMP.CASE_PARTIES_DROPDOWN" values="getCaseParties(null)"/-->
  </on-change>

</datagrid>
```

**Пример 2:** В этом примере выпадающее меню содержит всех подозреваемых, связанных с делом.
```xml
<field name="TEMP.SUSPECTS_DROPDOWN" type="dropdown"
      values="GetCaseParties(null, 'S')">
  <label>Suspects</label>
</field>
```



[На главную](./ecmfunctions/)