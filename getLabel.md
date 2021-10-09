#getLabel

---

Возвращает ярлык для определенного кода в справочной таблице.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | codeValue | указывает код, для которого используется ярлык. | String |
| 2 | referenceTableName | указывает имя в справочной таблице | String |

## Примеры

**Пример 1:** Задает значение поля для ярлыка события on-change.
```xml
<field name="X_SUSPECT.X_SUSPECT_ID_AUTHORITY_CD" type="dropdown" values="GetLabelValues('X_RT_SUSPECT_ID_AUTHORITY' + X_SUSPECT.X_SUSPECT_ID_AUTHORITY_TYPE_CD)">
   <label><message key="field.x_suspect.x_suspect_id_authority_cd.label.txt" /></label>
   <on-change>
      <set-value name="X_SUSPECT.X_SUSPECT_ID_AUTHORITY_TXT"
            value="GetLabel(X_SUSPECT.X_SUSPECT_ID_AUTHORITY_CD, 'X_RT_SUSPECT_ID_AUTHORITY' + X_SUSPECT.X_SUSPECT_ID_AUTHORITY_TYPE_CD)" />
   </on-change>
</field>
```

