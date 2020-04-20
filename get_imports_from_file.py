print("getting imports from file")
ea = 0x408000
end = 0x4081A4
filename = 'imports_{}_{}.txt'.format(hex(ea), hex(end))

with open(filename) as f:
	for line in f.readlines():
		name = line.strip()
		if len(name):
			set_name(ea, name)
		ea = next_head(ea)

print('imports written from file:{}'.format(filename))