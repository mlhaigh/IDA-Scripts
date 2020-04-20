print("writing imports to file")
ea = 0x408000
end = 0x4081A4
filename = 'imports_{}_{}.txt'.format(hex(ea), hex(end))

with open(filename, 'w') as f:
	while ea <= end:
		name = get_name(get_wide_dword(ea))
		#print(name)
		f.write(name + '\n')
		ea = next_head(ea)

print('exports written to file:{}'.format(filename))