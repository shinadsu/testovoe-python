import pandas as pd

# загрузка данных из файла test.csv
data = pd.read_csv('test.csv', delimiter=';')

# создание сводной таблицы
pivot_table = pd.pivot_table(data, 
                             index=['ym:s:lastTrafficSource', 'ym:s:referer'], 
                             values=['ym:s:users', 'ym:s:goalReachesAll', 'ym:s:goal47216452'],
                             aggfunc={'ym:s:users': 'sum', 
                                      'ym:s:goalReachesAll': 'sum', 
                                      'ym:s:goal47216452': 'sum'})

# вывод сводной таблицы
print(pivot_table)