# `/usr/lib/system/libunwind.dylib`

From the erase/recovery restore ramdisk (141-28940-105.dmg, runs restored_external). 128,864 bytes.

## Header

```
Magic         = 64-bit MachO
Type          = DYLIB
CPU           = AARCH64, 0xc caps: USR00
Commands      = 24 (Size: 1976)
Flags         = NoUndefs, DyldLink, TwoLevel, NoReexportedDylibs, AppExtensionSafe
```

## Linked libraries (7)

- `/usr/lib/system/libunwind.dylib (compatibility version 1.0.0, current version 2200.5.0)`
- `/usr/lib/system/libsystem_malloc.dylib (compatibility version 1.0.0, current version 886.40.15)`
- `/usr/lib/system/libsystem_c.dylib (compatibility version 1.0.0, current version 1786.40.6)`
- `/usr/lib/system/libdyld.dylib (compatibility version 0.0.0, current version 0.0.0)`
- `/usr/lib/system/libcompiler_rt.dylib (compatibility version 1.0.0, current version 103.4.0, upward)`
- `/usr/lib/system/libsystem_pthread.dylib (compatibility version 1.0.0, current version 553.40.2)`
- `/usr/lib/system/libsystem_platform.dylib (compatibility version 1.0.0, current version 402.40.3)`

## Entitlements

```xml
  - no entitlements
```

## Strings (138)

```
Bad unwind with PAuth-enabled ABI
getSavedFloatRegister
x15
x18
d24
CIE ID is not zero
libunwind: malformed DW_CFA_def_cfa_register DWARF unwind, reg too big\n
x4
x10
x24
d17
unsupported restore location for float register
libunwind: malformed DW_CFA_offset_extended DWARF unwind, reg too big\n
DW_OP_piece not implemented
d6
d29
d19
unsupported arm64 register
getULEB128
x11
x12
__unw_set_reg
x13
x25
lr
d3
d26
libunwind: malformed DW_CFA_expression DWARF unwind, reg too big\n
DW_EH_PE_datarel is invalid with a datarelBase of 0
DW_EH_PE_funcrel pointer encoding not supported
SME ZA disable failed
d27
invalid IP
x22
d21
stop unwinding
unsupported operation or bad value
unknown pointer encoding
x3
x9
d0
d16
_Unwind_GetTextRelBase
libunwind: malformed DW_CFA_restore_extended DWARF unwind, reg too big\n
libunwind: malformed DW_CFA_val_offset_sf DWARF unwind, reg too big\n
x20
libunwind: malformed DW_CFA_offset_extended_sf DWARF unwind, reg too big\n
libunwind: malformed DW_CFA_def_cfa_sf DWARF unwind, reg too big\n
libunwind: malformed DW_CFA_GNU_negative_offset_extended DWARF unwind, reg too big\n
DW_EH_PE_aligned pointer encoding not supported
_Unwind_Resume() can't return
invalid compact unwind encoding
libunwind: malformed DW_CFA_def_cfa DWARF unwind, reg too big\n
setRegister
libunwind: malformed DW_CFA_register DWARF unwind, reg too big\n
DW_OP_deref_size with bad size
d9
unknown register
CIE start does not match
libunwind: malformed DW_CFA_same_value DWARF unwind, reg too big\n
libunwind: malformed DW_CFA_val_offset DWARF unwind, reg (%llu) out of range\n\n
DWARF opcode not implemented
stepWithCompactEncoding
d8
_Unwind_Resume
x8
d12
CIE version is not 1 or 3
invalid error code
DW_OP_fbreg not implemented
x7
x23
d30
attempt to write read-only register
getEncodedP
DW_EH_PE_textrel pointer encoding not supported
x0
x17
d5
d25
d28
libunwind: malformed DW_CFA_undefined DWARF unwind, reg too big\n
d1
d23
unwind_phase2
d10
truncated uleb128 expression
zaDisable
x2
x16
d31
during phase1 personality function said it would stop here, but now in phase2 it did not stop here
unwind info has unsupported version
getRegister
truncated sleb128 expression
pc
x26
d13
evaluateExpression
unsupported restore location for register
x27
x28
fp
d7
libunwind: Bad unwind with PAuth-enabled ABI (0x%zX, 0x%zX)->0x%zX\n\n
bad frame
getSavedRegister
x5
d22
libunwind: %s - %s\n
unspecified (general) error
malformed uleb128 expression
d15
d18
_Unwind_GetTextRelBase() not implemented
getSLEB128
x1
x19
d2
d20
_Unwind_GetDataRelBase
_Unwind_GetDataRelBase() not implemented
libunwind: malformed DW_CFA_val_expression DWARF unwind, reg too big\n
out of memory
x6
d11
d14
no unwind info found
sp
d4
FDE is really a CIE
no error
bad register number
cross unwind with return address signing
libunwind: malformed DW_CFA_register DWARF unwind, reg2 too big\n
x14
x21
FDE has zero length
```
