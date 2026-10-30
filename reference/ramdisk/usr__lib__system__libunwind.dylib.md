# `/usr/lib/system/libunwind.dylib`

From the upgrade restore ramdisk (141-29011-104.dmg). 128,864 bytes.

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
libunwind: malformed DW_CFA_val_expression DWARF unwind, reg too big\n
x4
x16
x27
invalid error code
getULEB128
DW_OP_fbreg not implemented
x6
x14
x21
bad register number
d21
d27
CIE version is not 1 or 3
_Unwind_GetDataRelBase() not implemented
getRegister
x2
d0
d16
CIE ID is not zero
unspecified (general) error
bad frame
libunwind: malformed DW_CFA_expression DWARF unwind, reg too big\n
SME ZA disable failed
x8
d5
d29
d30
libunwind: malformed DW_CFA_restore_extended DWARF unwind, reg too big\n
libunwind: malformed DW_CFA_GNU_negative_offset_extended DWARF unwind, reg too big\n
x9
d24
CIE start does not match
malformed uleb128 expression
stepWithCompactEncoding
d20
_Unwind_GetTextRelBase
DWARF opcode not implemented
pc
x24
libunwind: Bad unwind with PAuth-enabled ABI (0x%zX, 0x%zX)->0x%zX\n\n
x22
unknown pointer encoding
getSLEB128
x26
d19
libunwind: malformed DW_CFA_offset_extended DWARF unwind, reg too big\n
libunwind: malformed DW_CFA_same_value DWARF unwind, reg too big\n
libunwind: malformed DW_CFA_register DWARF unwind, reg too big\n
libunwind: malformed DW_CFA_val_offset_sf DWARF unwind, reg too big\n
truncated sleb128 expression
DW_OP_deref_size with bad size
x1
stop unwinding
DW_EH_PE_funcrel pointer encoding not supported
fp
d12
d26
getEncodedP
x5
d6
libunwind: malformed DW_CFA_def_cfa_register DWARF unwind, reg too big\n
zaDisable
lr
d7
d31
unknown register
unsupported restore location for register
d17
d22
Bad unwind with PAuth-enabled ABI
x0
x15
x19
d2
no error
invalid IP
libunwind: malformed DW_CFA_def_cfa_sf DWARF unwind, reg too big\n
d15
unwind_phase2
evaluateExpression
DW_OP_piece not implemented
x7
d1
during phase1 personality function said it would stop here, but now in phase2 it did not stop here
getSavedFloatRegister
setRegister
libunwind: %s - %s\n
unsupported operation or bad value
x25
libunwind: malformed DW_CFA_offset_extended_sf DWARF unwind, reg too big\n
d11
_Unwind_GetTextRelBase() not implemented
DW_EH_PE_datarel is invalid with a datarelBase of 0
DW_EH_PE_aligned pointer encoding not supported
d10
d13
d25
FDE has zero length
attempt to write read-only register
unwind info has unsupported version
getSavedRegister
__unw_set_reg
x13
x17
d4
out of memory
invalid compact unwind encoding
x10
x11
x28
d8
unsupported arm64 register
libunwind: malformed DW_CFA_register DWARF unwind, reg2 too big\n
x12
d9
_Unwind_Resume() can't return
d18
x3
d14
_Unwind_GetDataRelBase
unsupported restore location for float register
no unwind info found
DW_EH_PE_textrel pointer encoding not supported
sp
x20
d28
_Unwind_Resume
libunwind: malformed DW_CFA_undefined DWARF unwind, reg too big\n
libunwind: malformed DW_CFA_def_cfa DWARF unwind, reg too big\n
libunwind: malformed DW_CFA_val_offset DWARF unwind, reg (%llu) out of range\n\n
truncated uleb128 expression
d3
d23
FDE is really a CIE
x18
x23
cross unwind with return address signing
```
