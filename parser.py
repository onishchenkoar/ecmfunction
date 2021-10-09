from itertools import zip_longest

from bs4 import BeautifulSoup
from markdownify import markdownify

with open('ecm_reference_functions.html', encoding='UTF-8') as f:
  soup = BeautifulSoup(f, features='lxml')

records = soup('div', attrs={'class' : 'mainSection'})
for record in records:
  name = record.h2.text.strip()
  markdown = f'# {name}\n\n---\n\n'

  description = record.find('div', attrs={'class' : 'description'}).text.strip()
  description = ' '.join(description.split())
  markdown += f'{description}\n\n'

  returns = record.find('div', attrs={'class' : 'details'}).text.strip()
  returns = ' '.join(word for word in returns.split(' ') if word)
  returns = returns.replace('\n ', '\n')
  markdown += f'#### {returns}\n\n'

  args = record.find('div', attrs={'class' : 'section-indent'}).table
  if args is None:
    args = 'Отсутствуют'
  else:
    args = str(args)
    args = ' '.join(word for word in args.split(' ') if word)
    args = args.replace('\n ', '\n')
    args = (
      args.replace('>\n<th', '><th')
          .replace('>\n<td', '><td')
          .replace('\n</tr', '</tr')
          .replace('tableData">\n', 'tableData">')
          .replace('\n</td', '</td')
          .replace('&lt;', '<')
          .replace('&gt;', '>')
    )
    args = markdownify(args).strip()
  markdown += f'## Аргументы\n\n{args}\n\n'

  lst = record('div', attrs={'class' : 'section-indent'})
  if len(lst) == 2:
    examples = lst[-1]
    markdown += f'## Примеры\n\n'
    for example, code in zip_longest(examples('div'), examples('pre')):
      ex_text = example.text.strip()
      ex_text = ' '.join(word for word in ex_text.split() if word)
      pos = ex_text.find(':')
      ex_text = '**' + ex_text[:pos+1] + '**' + ex_text[pos+1:]
      markdown += f'{ex_text}\n'
      code_text = f'```xml\n{code.text.strip()}\n```'
      markdown += f'{code_text}\n\n'
  else:
    examples = None

  with open(f'{record.h2.text.strip()}.md', 'w', encoding='UTF-8') as f:
    f.write(markdown)
