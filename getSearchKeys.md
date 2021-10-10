#getSearchKeys

---

Возвращает список ключей для свойств указанного типа.
Запрос на тип ключей строится из набора функций, таких как `QueryEquals()`, `QueryAnd()`, `QueryOr()`, `QueryLike()`, и т. д.
Это дает возможность использовать мощное и эффективное средство для получения сущностей соответствующих определенному критерию.
Распространённым случаем использования этой функции может быть отображение в таблице сущностей, удовлетворяющих определенному критерию.
Вы можете использовать эту функцию вместе с функциями `GetEntityListAsMapList()` и `GetEntities()` для заполнения данными компонента таблицы DataStore.

#### Возвращает:

`List<Long>`

Список всех соответствующих ключей сущностей.

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | entityType | Тип сущности, напр. REPORT, CASE, INCIDENT, PARTY | `string` |
| 2 | queryFunction | Комбинация функция `Query*()`, таких как `QueryEquals()`, `QueryAnd()`, `QueryOr()`, `QueryNot()`, `QueryLike()`, `QueryIn()`, и `QueryRange()`. | `expression` |
| 3 | sortFieldName | Имя поля по которому следует выполнять сортировку. Это не обязательный аргумент. | `string` |
| 4 | SortOrder | Требуемый порядок сортировки, 'ASC' или 'DESC'. Это не обязательный параметр. | `string` |

## Примеры

**Пример 1:** Заполнение данными компонента таблицы DataGrid всеми делами, созданными пользователем, аутентифицированным в данный момент в системе.
```xml
<datagrid name="cases.grid" selectedKeyField="TEMP.USER_ID">
   <datastore id="cases.grid.store"
         data="GetEntityListAsMapList(GetEntities('case',
                  GetSearchKeys('case',
                     if(empty(TEMP.SELECTED_USER),
                        QueryNull('CASE.CASE_RK', false),
                        QueryEquals('CASE.CREATE_USER_ID', GetUserId())
                     )
                  )
               ))"
   />
  ...
</datagrid>
```

**Пример 2:** Использование этой функции для возвращения всех клиентов с типом кода 'HDR'. Результаты сортируются по ID клиентов в порядке убывания.
```
GetSearchKeys('PARTY', QueryEquals('PARTY.PARTY_TYPE_CD', 'HDR'), 'PARTY.PARTY_ID', 'DESC')
```

**Пример 3:** Использование этой функции для возвращения всех клиентов с типом кода 'HDR и категорией кода 'SCN'. Результаты сортируются по ID клиентов в порядке возрастания.
```
GetSearchKeys(
  'PARTY',
  QueryAnd(QueryEquals('PARTY.PARTY_TYPE_CD', 'HDR'),
           QueryEquals('PARTY.PARTY_CATEGORY_CD', 'SCN')
          ),
  'PARTY.PARTY_ID',
  'ASC'
)
```

