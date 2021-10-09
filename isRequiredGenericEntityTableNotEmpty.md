#isRequiredGenericEntityTableNotEmpty

---

Используется для того, чтобы обеспечить наличие в компоненте a GenericEntityTable как минимум одной записи. Может использоваться для компонента GenericEntityTables, связанного с основным объектом, например делом, или другим компонентом GenericEntityTable.

#### Возвращает:

Boolean

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | parentRK | Первичный ключ родительского объекта, к которому привязан объект GenericEntityTable. | Long |
| 2 | fieldName | Имя поля в GenericEntityTable которое содержит один или несколько родительских ключей. | String |

## Примеры

**Пример 1:** В этом примере демонстрируется использование функции для того, чтобы принудительно обеспечить связь подозреваемого по делу с как минимум одним финансовым институтом, как это требуется для отчетности SAR.
```xml
<field name="TEMP.SUSPECT_RELATIONSHIP_TABLE" type="component" component-name="GenericEntityTable">

   <validation test="isRequiredGenericEntityTableNotEmpty(X_SUSPECT.X_SUSPECT_RK, 'X_SUSPECT_RELATION.X_SUSPECT_RK')">
      <errmsg>
         <message key="field.x_suspect_relation.x_suspect_rk.required.txt" />
      </errmsg>
   </validation>

   <param name="objectName" value="'CASE'" />
   <param name="tableName" value="'X_SUSPECT_RELATION'" />
   <param name="dialogScreenId" value="'suspectRelationship'" />
   <param name="filter" value="'X_SUSPECT_RK=' + X_SUSPECT.X_SUSPECT_RK" />

   <!-- The description of the entity that a row represents (e.g. "Suspect") (optional) -->
   <param name="rowTypeDescription" value="'Relationship to Financial Institution'" />

   <!-- The dimensions of the popup dialog used to edit/view row (optional) -->
   <param name="dialogWidth" value="600" />
   <param name="dialogHeight" value="500" />

   <!-- fields/columns that will be shown in table -->
   <param name="field" value="'X_SUSPECT_RELATION_CD:X_RT_SUSPECT_RELATION'" />
   <param name="field" value="'X_SUSPECT_RELATION_OTHER_TXT'" />

</field>
```

