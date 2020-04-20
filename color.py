import idc
from idc import *

currentEA = None
currentMnem = None
prevMnem = None
currentOp = None
prevMnem = ""
currentOp = None
currentEA = get_first_seg()
currentEA = next_head(currentEA, 0xFFFFFFFFFFFFFFFF)
while (currentEA != BADADDR):
    currentMnem = print_insn_mnem(currentEA);

    #Highlight call functions
    if (currentMnem == "call"):
        set_color(currentEA, CIC_ITEM, 0x585858 )
    #Non-zeroing XORs are often signs of data encoding
    if (currentMnem == "xor" or currentMnem == "pxor"):
        if (print_operand(currentEA, 0) != print_operand(currentEA, 1)):
            set_color(currentEA, CIC_ITEM, 0x800000)

    #Instructions used for Anti-VM, sidt, sgdt, sldt, smsw, str, in, cpuid
    if (currentMnem == "sidt" or currentMnem == "sgdt" or currentMnem == "sldt" or currentMnem == "smsw" or currentMnem == "str" or currentMnem == "in" or currentMnem == "cpuid"):
        set_color(currentEA, CIC_ITEM, 0xFFFF00)

    #Highlight interrupts in code as an anti-debugging measure
    if (currentMnem == "int" and (print_operand(currentEA, 0) == "3" or print_operand(currentEA, 0) == "2D")):
        set_color(currentEA, CIC_ITEM, 0xFFFF00)

    #Highlight push/ret combinations as a shellcode
    if (currentMnem == "ret" and prevMnem == "push"):
        set_color(currentEA, CIC_ITEM, 0xFFFF00)

    currentEA = next_head(currentEA, 0xFFFFFFFFFFFFFFFF)
    prevMnem = currentMnem
