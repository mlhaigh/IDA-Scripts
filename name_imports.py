for ea in range(0x416468, 0x41668C):
    if 'off' in Name(ea):
        addr = Dword(ea)   
        new_name = Name(Dword(ea))
        MakeName(ea, new_name+'_0')