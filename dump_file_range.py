print('Executing dump script')
data = []
start = 0x401000
end = 0x41E000
filename='dump_{}_{}'.format(hex(start), hex(end))

for ea in range(start, end):
    data.append(get_wide_byte(ea))
bytes = bytearray(data)

with open(filename, 'wb') as f:
	f.write(bytes)
print('dump written to file {}'.format(filename))