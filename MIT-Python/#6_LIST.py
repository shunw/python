Techs=['MIT', 'Cal Tech']
Ivys=['Harvard', 'Yale', 'Brown']
Univs=[]
# Univs.append(Techs)
# Univs.append(Ivys)

# for e in Univs:
# 	print e
# 	for c in e:
# 		print c
Univs=Techs+Ivys
Ivys.remove('Harvard')
print Univs
print Ivys
