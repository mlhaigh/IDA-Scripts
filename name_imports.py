for ea in range(0x73116a2c, 0x73116aa8):
    if 'off' in get_name(ea):
        addr = get_wide_dword(ea)   
        new_name = get_name(get_wide_dword(ea))
        set_name(ea, new_name+'_0')