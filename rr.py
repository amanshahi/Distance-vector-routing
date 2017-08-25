import os
with open('out') as f:
	x = f.readlines()
x, g = x[0].split(), -123
for i in range(len(x)):
	if x[i] == 'python':
		g = x[i-3]
		break
if g != -123:
	s = "kill -9 "+g
	os.system(s)
	os.system("ps")