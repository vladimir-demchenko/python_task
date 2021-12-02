"""
1) Создать текстовый txt-файл.
2) Вставить туда англоязычную статью из Википедии.
3) Написать функцию со следующим функционалом:
3.1) Прочитать файл построчно, вывести на печать.
3.2) Создать список и добавить туда непустые строки.
3.3) В строках оставить только латинские буквы и пробелы. Прочие символы удалить.
3.4) Объединить список в единую строку. вывести на печать.
3.5) Подсчитать количество вхождений различных слов в тескте. Подсчет вести в словаре.
3.6) Вывести на печать 10 наиболее популярных и наименее популярных слов (“ 1) -- hello -- 15”).
3.7) Заменить наименее популярные слова на “PYTHON”.
3.8) Создать новый txt-файл.
3.9) Записать текст в файл, разбивая на строки, при этом на каждой строке записывать не более 100 символов и не делить слова.
"""

def view_file_3_1(f): 
  lines = f.readlines() 
  for i in lines: 
    print(i) 
  return lines

def delete_empty_lines_3_2(lines): 
  tmp = [] 
  for i in lines: 
    i = i.replace('\n', '') 
    if i != '': 
      tmp.append(i) 
  return tmp

def delete_symbols_3_3(lines): 
  for i in range(len(lines)): 
    tmp = [] 
    for j in range(len(lines[i])): 
      t = lines[i][j]
      if not(t is ' ' or t.isalpha()): 
        tmp.append(t) 
    for k in tmp: 
      lines[i] = lines[i].replace(k, '') 
  return lines

def one_line_print_3_4(lines): 
  one = ' '.join(lines) 
  print(one) 
  return one

def statistic_3_5(one_line): 
  one_list = one_line.split(' ') 
  stat = {} 
  for i in one_list:  
    if stat.get(i): 
      stat[i] += 1 
    else: 
      stat.update({i: 1}) 
  return stat

def sort_key(e): 
  return e[1]

def print_top_and_bottom_3_6(stat): 
  l = [] 
  for key, value in stat.items(): 
    l.append([key, value])
  l = sorted(l, key=sort_key, reverse=1)
  print("------TOP-10------") 
  i = 1 
  for key, value in l[:10]: 
    print("{}) -- {} -- {}".format(i, key, value)) 
    i += 1 
  print("------BOTTOM-10---") 
  j = len(l) 
  for key, value in l[-10:]: 
    print("{}) -- {} -- {}".format(j, key, value)) 
    j -= 1 
  return l

def change_minimal_3_7(one_line, score): 
  tmp = one_line.split(' ') 
  score = sorted(score, key=sort_key) 
  minimum = score[0][1] 
  for i in range(len(tmp)): 
    for j in score: 
      if tmp[i].lower() == j[0] and j[1] == minimum: 
        tmp[i] = 'PYTHON' 
  return tmp

def create_new_file_3_8(name): 
  f = open(name, 'w') 
  return f

def write_text_3_9(f, text): 
  l = '' 
  tmp = [] 
  t = 0 
  for i in text: 
    word_len = len(i) 
    if t + word_len < 100: 
      l += i + ' ' 
      t += word_len + 1 
    else: 
      l += '\n' 
      tmp.append(l)
      l = '' 
      t = 0 
  for j in tmp: f.write(j)

def wiki_function(file_name): 
  with open(file_name, 'r') as f: 
    lines = view_file_3_1(f) 
    lines = delete_empty_lines_3_2(lines) 
    lines = delete_symbols_3_3(lines) 
    one_line = one_line_print_3_4(lines) 
    stat = statistic_3_5(one_line) 
    score = print_top_and_bottom_3_6(stat) 
    text = change_minimal_3_7(one_line, score) 
    w = create_new_file_3_8('output.txt') 
    write_text_3_9(w, text) 
    w.close()

wiki_function('test.txt')