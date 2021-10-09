#getCaseSubjectRelationships

---

Эта функция не используется начиная с версии Enterprise Case Management 6.1.
Компонент CasePartiesTable, который использует эта функция, был заменен компонентом CasePartiesGrid.
Эта функция всегда возвращает пустой список.
В качестве замены этой функции на функцию, которая может использоваться с CasePartiesGrid вы можете использовать XXX.

#### Возвращает:

Map<Long, List<com.sas.solutions.casemgmt.domain.EntityRelationshipEntity<com.sas.solutions.casemgmt.domain.Party>>>

## Аргументы

|  | Имя аргумента | Описание | Тип значения |
| --- | --- | --- | --- |
| 1 | casePartyTableName | Имя компонента CasePartyTable в контексте. | `String` |
| 2...n | filterCodeValue | Значения для кода, используемые для отбора возвращаемых типов отношений. Значения должны соответствовать значениям, заданным в настраиваемых таблицах поиска, которые передаются в компонент CasePartyTable в параметре 'relationship\_type\_table'. | `String` |

