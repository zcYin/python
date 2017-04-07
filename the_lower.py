L1 = ['Hello','World',18,'IBM','Apple']
L2 = []

for x in L1:
	if isinstance(x,str):
		L2.append(x)
print([s.lower() for s in L2])