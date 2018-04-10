"""import pandas

csv = pandas.read_csv('data/data_random.csv', sep=',', skipinitialspace=False, error_bad_lines=False)

csv_b = csv[csv['diagnosis'] == 'B']
csv_m = csv[csv['diagnosis'] == 'M']

csv_b.to_csv('data/b_all.csv', index=False, sep=',')
csv_m.to_csv('data/m_all.csv', index=False, sep=',')"""

b_train_n = 286
b_test_n = 71

m_train_n = 170
m_test_n = 42

b_all = open('data/b_all.csv', 'r')
b_train = open('data/b_train.csv', 'w')
b_test = open('data/b_test.csv', 'w')

m_all = open('data/m_all.csv', 'r')
m_train = open('data/m_train.csv', 'w')
m_test = open('data/m_test.csv', 'w')

c = 0
for row in b_all:
	if c >= b_train_n:
		b_test.write(row)
	else:
		b_train.write(row)
		c+=1

c = 0
for row in m_all:
	if c >= m_train_n:
		m_test.write(row)
	else:
		m_train.write(row)
		c+=1