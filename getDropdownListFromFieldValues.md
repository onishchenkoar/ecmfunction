# getDropdownListFromFieldValues

---

Возвращает упорядоченный список `java.util.Collection` объектов `org.apache.struts.util.LabelValueBean` с ярлыками и
значениями для выпадающего списка.

#### Возвращает:

Неизвестно

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | labelField | указывает имя поля для ярлыков. | `String` |
| 2 | valueField | указывает имя поля для значений. | `String` |

## Примеры

**Пример 1:** Заполнение выпадающего списка всеми значениями для поля.
```xml
<field
  name="PARTY.X_FILE_NM"
  type="dropdown"
  readonly="true"
  values="GetDropdownListFromFieldValues('TEMP.FILE_NM','TEMP.FILE_NM')"
>
   <label>
     <message key="field.party_x_file_name.label.txt" />
   </label>
</field>
```



[На главную](./ecmfunctions/)